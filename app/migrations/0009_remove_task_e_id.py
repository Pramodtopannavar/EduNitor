# Generated by Django 5.1.7 on 2025-04-06 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_task_e_id_task_e_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='e_id',
        ),
    ]
