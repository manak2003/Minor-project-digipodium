# Generated by Django 4.1.1 on 2022-12-07 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_job_how_quickly_do_you_need_to_hire'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='job_benefits',
            field=models.CharField(default=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='job',
            name='job_requirements',
            field=models.CharField(default=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_description',
            field=models.CharField(default=True, max_length=1000),
        ),
    ]