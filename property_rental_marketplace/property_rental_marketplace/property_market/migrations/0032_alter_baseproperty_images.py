# Generated by Django 4.2.2 on 2023-08-05 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property_market', '0031_alter_baseproperty_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseproperty',
            name='images',
            field=models.FileField(upload_to='property_images'),
        ),
    ]