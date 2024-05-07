# Generated by Django 5.0 on 2024-05-03 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=10, null=True)),
                ('full_name', models.CharField(default='anomynous', max_length=100)),
                ('score1', models.DecimalField(decimal_places=1, default=0.0, max_digits=3)),
                ('score2', models.DecimalField(decimal_places=1, default=0.0, max_digits=3)),
                ('midterm', models.DecimalField(decimal_places=1, default=0.0, max_digits=3)),
                ('final', models.DecimalField(decimal_places=1, default=0.0, max_digits=3)),
            ],
        ),
    ]
