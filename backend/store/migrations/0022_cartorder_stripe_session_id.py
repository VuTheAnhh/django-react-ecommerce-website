# Generated by Django 5.0 on 2024-04-14 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_cartorderitem_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorder',
            name='stripe_session_id',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]