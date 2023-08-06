import json
import logging
import os.path
import shutil
import zipfile

import django_rq

# from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from guardian.decorators import permission_required_or_403
from openlink.core.connector import Mapper
from openlink.core.models import (
    Assay,
    Dataset,
    Investigation,
    Mappableobject,
    Mapping,
    MappingProjectUser,
    Project,
    Study,
    Tool,
)

logger = logging.getLogger(__name__)


@permission_required_or_403("change_project", (Project, "id", "project_id"))
def choose_object_to_publish(request, *args, **kwargs):
    # select objects to publish and get information from connector
    current_proj = kwargs["project_id"]
    project = get_object_or_404(Project, id=current_proj)
    investigation = get_object_or_404(Investigation, pk=kwargs["pk"])
    mappinginv = Mapping.objects.filter(foreign_id_obj__id=investigation.id)

    tags = []
    users = []
    listi = []
    mixedlist = []

    if request.method == "POST":
        if mappinginv:
            for name in mappinginv:
                tool_qs = get_object_or_404(Tool, mapping=name)
                connector2 = tool_qs.get_connector()
                if issubclass(connector2.__class__, Mapper):
                    information = connector2.get_information(name.type, name.object_id)
                    if "tags" in information:
                        for tag in information["tags"]:
                            tags.append(tag)
                    if "user" in information:
                        for user in information["user"]:
                            users.append(user)

        tomap = []
        for item in request.POST:
            if item != "csrfmiddlewaretoken":
                tomap.append(item)
                mappi = Mapping.objects.filter(foreign_id_obj__id=item, type="dataset")
                if mappi:
                    name = mappi[0]
                    mixedlist.append(name)
                    tool_qs = get_object_or_404(Tool, mapping=name)
                    connector2 = tool_qs.get_connector()
                    if issubclass(connector2.__class__, Mapper):
                        information = connector2.get_information(
                            name.type, name.object_id
                        )
                        if "tags" in information:
                            for tag in information["tags"]:
                                tags.append(tag)
                        if "user" in information:
                            for user in information["user"]:
                                users.append(user)
                try:
                    name = Study.objects.get(pk=item)
                except Study.DoesNotExist:
                    try:
                        name = Assay.objects.get(pk=item)
                    except Assay.DoesNotExist:
                        name = Dataset.objects.get(pk=item)
                listi.append(name)
                mixedlist.append(name)
                if mappi:
                    mixedlist.pop()
        tagstring = ""
        for tag in tags:
            tagstring += tag
            tagstring += ","
        openlinkusers = MappingProjectUser.objects.filter(project=project)
        for openlinkuser in openlinkusers:
            users.append(str(openlinkuser.user))
        users = list(set(users))
        # fmt: off
        for iduser, user in enumerate(users[:-1]):
            dec = 0
            try:
                users[iduser]
            except Exception:
                break
            forcomp = []
            if " " in users[iduser]:
                usersep = users[iduser].split(" ")
                forcomp.append((usersep[1] + " " + usersep[0]).lower())  # 2
                forcomp.append((usersep[1][0] + " " + usersep[0]).lower())  # 3
                forcomp.append((usersep[0][0] + " " + usersep[1]).lower())  # 4
                forcomp.append((usersep[1] + " " + usersep[0][0]).lower())  # 5
                forcomp.append((usersep[0] + " " + usersep[1][0]).lower())  # 6
                forcomp.append((usersep[1][0] + usersep[0]).lower())  # 7
                forcomp.append((usersep[0][0] + usersep[1]).lower())  # 8
                forcomp.append((usersep[1] + usersep[0][0]).lower())  # 9
                forcomp.append((usersep[0] + usersep[1][0]).lower())  # 10
            forcomp.append(users[iduser].lower())  # 1
            for idcomp, compa in enumerate(users[iduser + 1:]):
                for comp in forcomp:
                    if comp == users[idcomp + iduser + 1 - dec].lower():
                        if len(users[idcomp + iduser + 1 - dec]) > len(users[iduser]):
                            users[iduser] = users[idcomp + iduser + 1 - dec]
                        users.pop(idcomp + iduser + 1 - dec)
                        dec += 1
        # fmt: on
        logging.debug(mixedlist)
        return render(
            request,
            "publish/choose_metadata.html",
            {
                "title": investigation,
                "tags": tagstring,
                "list": listi,
                "listmap": mixedlist,
                "users": users,
                "tomap": tomap,
                "project": project,
            },
        )
    return render(
        request,
        "publish/choose_object_to_publish.html",
        {"items": investigation, "project": project},
    )


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(
                os.path.join(root, file),
                os.path.relpath(os.path.join(root, file), os.path.join(path, "..")),
            )


@permission_required_or_403("change_project", (Project, "id", "project_id"))
def choose_metadata(request, *args, **kwargs):
    # get metadata and start asynchronous publication
    current_proj = kwargs["project_id"]
    project = get_object_or_404(Project, id=current_proj)
    if request.method == "POST":
        queue = django_rq.get_queue("default")
        queue.enqueue(tool_to_tool, request.POST, project, kwargs)
        return HttpResponseRedirect(
            reverse("core:projects-details", kwargs={"project_id": current_proj})
        )


def tool_to_tool(request, project, kwargs):
    # download dataset and create depo with metadata
    tabstring = request["datatoup"]
    tabstring = tabstring.replace("'", '"')
    tab = json.loads(tabstring)
    title = request["title"]
    path = "openlink/core/lib/tools/tmp"
    if not os.path.exists("%s/%s" % (path, title)):
        os.makedirs("%s/%s" % (path, title))
        path = "%s/%s" % (path, title)
    level = ("investigation", "study", "assay")
    intlevel = 0
    for item in tab:
        mappi = Mapping.objects.filter(foreign_id_obj__id=item, type="dataset")
        if mappi.exists():
            name = mappi[0]
            tool_qs = get_object_or_404(Tool, mapping=name)
            connector2 = tool_qs.get_connector()
            object_id = name.object_id
        try:
            name = Study.objects.get(pk=item)
            level_ob = "study"
        except Study.DoesNotExist:
            try:
                name = Assay.objects.get(pk=item)
                level_ob = "assay"
            except Assay.DoesNotExist:
                name = Dataset.objects.get(pk=item)
                level_ob = "dataset"
        if level_ob == "dataset":
            # Download datasets
            if mappi.exists():
                try:
                    connector2.download(object_id, path)
                except Exception:
                    pass

        elif level[intlevel] == level_ob:
            path = path.rsplit("/", 1)[0]
            if not os.path.exists("%s/%s" % (path, name)):
                os.makedirs("%s/%s" % (path, name))
                path = "%s/%s" % (path, name)
        try:
            if level[intlevel - 1] == level_ob:
                path = path.rsplit("/", 1)[0]
                path = path.rsplit("/", 1)[0]
                if not os.path.exists("%s/%s" % (path, name)):
                    os.makedirs("%s/%s" % (path, name))
                    path = "%s/%s" % (path, name)
                intlevel -= 1
        except Exception:
            pass
        try:
            if level[intlevel + 1] == level_ob:
                if not os.path.exists("%s/%s" % (path, name)):
                    os.makedirs("%s/%s" % (path, name))
                    path = "%s/%s" % (path, name)
                    intlevel += 1
        except Exception:
            pass
    mappi = None
    # Create zipfile
    zipf = zipfile.ZipFile(
        "openlink/core/lib/tools/tmp/%s.zip" % title,
        "w",
        zipfile.ZIP_DEFLATED,
    )
    zipdir("openlink/core/lib/tools/tmp/%s" % title, zipf)
    zipf.close()
    shutil.rmtree("openlink/core/lib/tools/tmp/%s" % title)
    tagtab = request["tags"].split(",")
    tools_qs = Tool.objects.filter(project=project, id=kwargs["tool_id"])
    for tool in tools_qs:
        connector = tool.get_connector()
    creator = {}
    creators = []
    for post in request:
        if post.startswith("auth"):
            creator = {"name": request[post]}
        if post.startswith("affi"):
            if request[post]:
                creator.update({"affiliation": request[post]})
            creators.append(creator)
    metadata = {
        "metadata": {
            "title": title,
            "upload_type": request["type"],
            "description": request["description"],
            "creators": creators,
            "keywords": tagtab,
        }
    }
    # Add metadata to deposit
    if "saved_doi" not in kwargs:
        r = connector.create_empty_depo()
        path_to_file = "openlink/core/lib/tools/tmp/%s.%s" % (title, "zip")
        connector.add_file_to_depo(r, path_to_file)
        jsonr = connector.add_metadata_to_depo(metadata, r["links"]["self"])

        r = connector.publish_depo(jsonr)

        listitem = (
            request["list"]
            .replace("[", "")
            .replace("]", "")
            .replace("'", "")
            .split(",")
        )
        for item in listitem:
            try:
                mappi = Mapping.objects.filter(foreign_id_obj__id=item, type="dataset")
                if mappi.exists():
                    origin_object = get_object_or_404(Mappableobject, id=item)
                    new_mapping_object = Mapping()
                    new_mapping_object.name = title
                    new_mapping_object.tool_id = tool
                    new_mapping_object.type = "dataset"
                    new_mapping_object.object_id = r.json()["doi"]
                    new_mapping_object.foreign_id_obj = origin_object
                    new_mapping_object.save()
            except Dataset.DoesNotExist:
                pass

        new_mapping_inv = Mapping()
        new_mapping_inv.name = title
        new_mapping_inv.tool_id = tool
        new_mapping_inv.type = "investigation"
        new_mapping_inv.object_id = r.json()["doi"]
        new_mapping_inv.foreign_id_obj = get_object_or_404(
            Mappableobject, id=kwargs["pk"]
        )
        new_mapping_inv.save()

        os.remove("openlink/core/lib/tools/tmp/%s.%s" % (title, "zip"))
    else:
        r = connector.update_depo(str(kwargs["saved_doi"]), metadata)
    return HttpResponseRedirect(
        reverse(
            "core:projects-details",
            kwargs={"project_id": kwargs["project_id"]},
        )
    )
