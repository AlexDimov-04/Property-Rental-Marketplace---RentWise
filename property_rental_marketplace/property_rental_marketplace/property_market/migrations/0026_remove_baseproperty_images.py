# Generated by Django 4.2.2 on 2023-08-05 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property_market', '0025_alter_baseproperty_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseproperty',
            name='images',
        ),
    ]
