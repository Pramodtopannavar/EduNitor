# Generated by Django 5.1.7 on 2025-04-13 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_screenshotsmonitoring_ssm_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screenshotsmonitoring',
            name='ssm_log_ts',
            field=models.DateTimeField(),
        ),
    ]
