# Generated by Django 4.2.4 on 2023-08-04 10:16

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("name", models.CharField(max_length=500)),
                ("profile_picture", models.ImageField(upload_to="profile_pictures/")),
                ("description", models.TextField()),
                ("age", models.PositiveIntegerField()),
                ("email", models.EmailField(max_length=254)),
                ("linkedin_link", models.URLField(blank=True, null=True)),
                ("github_link", models.URLField(blank=True, null=True)),
                ("instagram_link", models.URLField(blank=True, null=True)),
            ],
        ),
    ]
