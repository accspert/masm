# Generated by Django 4.1.1 on 2023-04-07 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_course_day_of_week_course_end_time_course_start_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course", name="end_time", field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="course",
            name="start_time",
            field=models.DateTimeField(null=True),
        ),
    ]
