# Generated by Django 5.0 on 2024-04-07 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_alter_product_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('rate', models.IntegerField(default=5, help_text='Numbers added here are in percentage e.g 5%')),
                ('active', models.BooleanField(default=True)),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
