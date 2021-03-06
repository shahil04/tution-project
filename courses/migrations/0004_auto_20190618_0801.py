# Generated by Django 2.2 on 2019-06-18 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_delete_full_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursesdata',
            name='additional_title3',
        ),
        migrations.RemoveField(
            model_name='coursesdata',
            name='additional_topic3',
        ),
        migrations.RemoveField(
            model_name='coursesdata',
            name='overview_titles',
        ),
        migrations.RemoveField(
            model_name='coursesdata',
            name='read_more',
        ),
        migrations.RemoveField(
            model_name='coursesdata',
            name='syllabus_title',
        ),
        migrations.RemoveField(
            model_name='coursesdata',
            name='training_methodology_title',
        ),
        migrations.RemoveField(
            model_name='coursesdata',
            name='upcoming_batches_title',
        ),
        migrations.AlterField(
            model_name='coursesdata',
            name='additional_title1',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='coursesdata',
            name='additional_title2',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
