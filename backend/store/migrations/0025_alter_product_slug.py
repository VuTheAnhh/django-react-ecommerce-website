# Generated by Django 5.0.3 on 2024-04-29 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_rename_payment_cartorder_payment_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
