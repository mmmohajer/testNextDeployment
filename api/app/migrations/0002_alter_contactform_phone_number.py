# Generated by Django 4.0.2 on 2022-07-31 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
