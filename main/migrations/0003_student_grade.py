# Generated by Django 4.1.1 on 2023-04-07 10:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_alter_student_birthdate_alter_teacher_birthdate"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="grade",
            field=models.PositiveIntegerField(
                null=True, validators=[django.core.validators.MaxValueValidator(15)]
            ),
        ),
    ]
