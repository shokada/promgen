# Generated by Django 2.0.7 on 2018-07-31 08:09

from django.db import migrations
from django.conf import settings


def create_group(apps, schema_editor):
    if not settings.PROMGEN_DEFAULT_GROUP:
        return

    # Create Default Group
    group, created = apps.get_model("auth", "Group").objects.get_or_create(
        name=settings.PROMGEN_DEFAULT_GROUP
    )

    # Create default permissions. We skip the permissions that are
    # generally for admin rules (Shards, Prometheus, Audit) and skip
    # custom permissions for label/annotations but list everything else
    Permission = apps.get_model("auth", "Permission")
    group.permissions.set(
        Permission.objects.filter(
            content_type__app_label="promgen",
            content_type__model__in=[
                "exporter",
                "farm",
                "host",
                "project",
                "rule",
                "sender",
                "service",
                "url",
            ],
        )
    )

    # Add users to default group
    User = apps.get_model("auth", "User")
    for user in User.objects.all():
        user.groups.add(group)


def remove_group(apps, schema_editor):
    apps.get_model("auth", "Group").objects.filter(
        name=settings.PROMGEN_DEFAULT_GROUP
    ).delete()


class Migration(migrations.Migration):

    dependencies = [("promgen", "0002_auto_20180316_0525")]

    operations = [migrations.RunPython(create_group, remove_group)]
