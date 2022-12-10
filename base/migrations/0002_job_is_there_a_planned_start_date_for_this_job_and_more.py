# Generated by Django 4.1.1 on 2022-11-28 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='is_there_a_planned_start_date_for_this_job',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AddField(
            model_name='job',
            name='job_description',
            field=models.CharField(default=True, max_length=200),
        ),
        migrations.AddField(
            model_name='job',
            name='what_is_the_job_type',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AddField(
            model_name='job',
            name='what_is_the_pay',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='job',
            name='what_is_the_schedule_for_this_job',
            field=models.CharField(default=True, max_length=100),
        ),
    ]