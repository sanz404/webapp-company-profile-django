# Generated by Django 3.2.7 on 2022-07-23 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0008_auto_20220723_0750'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='person',
            name='api_app_per_is_admi_102399_idx',
        ),
        migrations.RemoveField(
            model_name='person',
            name='is_admin',
        ),
    ]
