# Generated by Django 2.1.2 on 2018-11-28 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("promgen", "0005_project_owner"),
    ]

    operations = [
        migrations.CreateModel(
            name="DefaultExporter",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("job", models.CharField(max_length=128)),
                ("port", models.IntegerField()),
                ("path", models.CharField(blank=True, max_length=128)),
            ],
            options={"ordering": ["job", "port"],},
        ),
        migrations.AlterUniqueTogether(
            name="defaultexporter", unique_together={("job", "port", "path")},
        ),
    ]
