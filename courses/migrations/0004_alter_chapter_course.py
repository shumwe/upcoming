# Generated by Django 4.1 on 2022-08-15 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0003_alter_course_featured_image_alter_course_sub_heading"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chapter",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="chapters",
                to="courses.course",
            ),
        ),
    ]
