# Generated by Django 4.1.5 on 2023-02-19 14:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseschedule',
            name='day',
        ),
        migrations.RemoveField(
            model_name='courseschedule',
            name='timeslots',
        ),
        migrations.AddField(
            model_name='courseschedule',
            name='day_of_week',
            field=models.CharField(choices=[('MON', 'Monday'), ('TUE', 'Tuesday'), ('WED', 'Wednesday'), ('THU', 'Thursday'), ('FRI', 'Friday'), ('SAT', 'Saturday'), ('SUN', 'Sunday')], default=django.utils.timezone.now, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='courseschedule',
            name='end_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='courseschedule',
            name='start_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='course',
            name='instructor_name',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='TimeSlot',
        ),
    ]
