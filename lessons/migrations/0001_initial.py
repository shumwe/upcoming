# Generated by Django 4.1 on 2022-08-13 18:06

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
    ]

    operations = [
        migrations.CreateModel(
            name="Lesson",
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
                ("name", models.CharField(max_length=155)),
                ("slug", models.SlugField(blank=True, max_length=160, null=True)),
                (
                    "featured_image",
                    models.ImageField(
                        default="not_available.png", upload_to="lesson_image"
                    ),
                ),
                ("author", models.CharField(max_length=55)),
                ("content", models.TextField()),
                ("publish", models.BooleanField(default=True)),
                ("posted", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "tags",
                    taggit.managers.TaggableManager(
                        help_text="A comma-separated list of tags.",
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="Tags",
                    ),
                ),
            ],
        ),
    ]
