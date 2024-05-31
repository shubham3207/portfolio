# Generated by Django 5.0.6 on 2024-05-30 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, null=True)),
                ("email", models.EmailField(max_length=200, null=True)),
                ("phone", models.CharField(max_length=200, null=True)),
                ("message", models.TextField(max_length=700, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "projectimg",
                    models.ImageField(blank=True, null=True, upload_to="media"),
                ),
                ("title", models.CharField(max_length=200)),
            ],
        ),
    ]