# Generated by Django 5.0 on 2024-04-02 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0005_user_reset_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='reset_token',
        ),
    ]
