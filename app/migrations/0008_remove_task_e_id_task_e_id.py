# Generated by Django 5.0.4 on 2025-03-02 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_delete_groupchat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='e_id',
        ),
        migrations.AddField(
            model_name='task',
            name='e_id',
            field=models.ManyToManyField(to='app.employee'),
        ),
    ]
