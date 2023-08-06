from openlink.core.models import (
    Assay,
    Dataset,
    Investigation,
    Mappableobject,
    Mapping,
    Study,
)
from rest_framework import serializers


class MappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mapping
        fields = ["name", "tool_id", "object_id", "foreign_id_obj"]
        depth = 2


class MappableobjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mappableobject
        fields = ["id"]
        depth = 1


class DatasetSerialiser(MappableobjectSerializer):
    data = serializers.SerializerMethodField()

    class Meta(MappableobjectSerializer.Meta):
        model = Dataset
        fields = ["data"]

    def get_data(self, obj):
        list_map = []

        qs_maps = Mapping.objects.filter(foreign_id_obj=obj.id)
        for qs_map in qs_maps:
            obj_type = qs_map.type
            obj_id = qs_map.object_id
            connector = qs_map.tool_id.get_connector()
            txt_to_add = {
                "tool": qs_map.tool_id.name,
                "tool_id": qs_map.tool_id.id,
                "obj_id": obj_id,
                "url": connector.get_url_link_to_an_object(obj_type, obj_id),
            }
            list_map.append(txt_to_add)

        return {
            "type": obj_type,
            "id": obj.pk,
            "name": obj.name,
            "mapping": list_map,
        }


class AssaySerializer(MappableobjectSerializer):
    dataset = DatasetSerialiser(many=True)
    data = serializers.SerializerMethodField()

    class Meta(MappableobjectSerializer.Meta):
        model = Assay
        fields = ["data", "dataset"]

    def get_data(self, obj):
        list_map = []

        qs_maps = Mapping.objects.filter(foreign_id_obj=obj.id)
        for qs_map in qs_maps:
            obj_type = qs_map.type
            obj_id = qs_map.object_id
            connector = qs_map.tool_id.get_connector()
            txt_to_add = {
                "tool": qs_map.tool_id.name,
                "tool_id": qs_map.tool_id.id,
                "obj_id": obj_id,
                "url": connector.get_url_link_to_an_object(obj_type, obj_id),
            }
            list_map.append(txt_to_add)

        return {
            "type": obj_type,
            "id": obj.pk,
            "name": obj.name,
            "mapping": list_map,
        }


class StudySerializer(MappableobjectSerializer):
    assay = AssaySerializer(many=True)
    data = serializers.SerializerMethodField()

    class Meta(MappableobjectSerializer.Meta):
        model = Study
        fields = ["data", "assay"]

    def get_data(self, obj):
        list_map = []

        qs_maps = Mapping.objects.filter(foreign_id_obj=obj.id)
        for qs_map in qs_maps:
            obj_type = qs_map.type
            obj_id = qs_map.object_id
            connector = qs_map.tool_id.get_connector()
            txt_to_add = {
                "tool": qs_map.tool_id.name,
                "tool_id": qs_map.tool_id.id,
                "obj_id": obj_id,
                "url": connector.get_url_link_to_an_object(obj_type, obj_id),
            }
            list_map.append(txt_to_add)

        return {
            "type": obj_type,
            "id": obj.pk,
            "name": obj.name,
            "mapping": list_map,
        }


class InvestigationSerializer(MappableobjectSerializer):
    study = StudySerializer(many=True)
    dataset = DatasetSerialiser(many=True)
    data = serializers.SerializerMethodField()

    class Meta(MappableobjectSerializer.Meta):
        model = Investigation
        fields = ["data", "study", "dataset"]

    def get_data(self, obj):
        list_map = []
        qs_maps = Mapping.objects.filter(foreign_id_obj=obj.id)
        for qs_map in qs_maps:
            obj_type = qs_map.type
            obj_id = qs_map.object_id
            connector = qs_map.tool_id.get_connector()
            txt_to_add = {
                "tool": qs_map.tool_id.name,
                "tool_id": qs_map.tool_id.id,
                "obj_id": obj_id,
                "url": connector.get_url_link_to_an_object(obj_type, obj_id),
            }
            list_map.append(txt_to_add)

        return {
            "type": "investigation",
            "id": obj.pk,
            "name": obj.name,
            "mapping": list_map,
        }


class ProjectSerializer(MappableobjectSerializer):
    investigation = InvestigationSerializer(many=True)
    data = serializers.SerializerMethodField()

    class Meta(MappableobjectSerializer.Meta):
        model = Investigation
        fields = ["data", "investigation"]

    def get_data(self, obj):
        list_map = []
        qs_maps = Mapping.objects.filter(foreign_id_obj=obj.id)
        for qs_map in qs_maps:
            obj_type = qs_map.type
            obj_id = qs_map.object_id
            connector = qs_map.tool_id.get_connector()
            txt_to_add = {
                "tool": qs_map.tool_id.name,
                "tool_id": qs_map.tool_id.id,
                "obj_id": obj_id,
                "url": connector.get_url_link_to_an_object(obj_type, obj_id),
            }
            list_map.append(txt_to_add)

        return {
            "type": "project",
            "id": obj.pk,
            "name": obj.name,
            "mapping": list_map,
        }
