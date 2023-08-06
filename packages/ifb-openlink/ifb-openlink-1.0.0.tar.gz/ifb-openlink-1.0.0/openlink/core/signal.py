import logging

import django.dispatch
from django.apps import apps
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from openlink.core.models import Mapping, Tool

logger = logging.getLogger(__name__)

signal = django.dispatch.Signal()
new_mapping_signal = django.dispatch.Signal()
delete_signal = django.dispatch.Signal()


@receiver(pre_delete, sender=Mapping)
def delete__signal(sender, **kwargs):
    mapping = kwargs["instance"]
    item = apps.get_model("core", str(mapping.type)).objects.get(
        id=mapping.foreign_id_obj.id
    )
    connector = Tool.objects.get(mapping__id=mapping.id).get_connector()
    delete_signal.send_robust(
        apps.get_model("core", str(mapping.type)),
        del_mapping=mapping,
        item=item,
        connector=connector,
    )


@receiver(post_save, sender=Mapping)
def new_map_signal(sender, **kwargs):
    logger.debug("new map")
    mapping = kwargs["instance"]
    item = apps.get_model("core", str(mapping.type)).objects.get(
        id=mapping.foreign_id_obj.id
    )
    connector = Tool.objects.get(mapping__id=mapping.id).get_connector()
    new_mapping_signal.send_robust(
        apps.get_model("core", str(mapping.type)),
        new_mapping=mapping,
        item=item,
        connector=connector,
    )
