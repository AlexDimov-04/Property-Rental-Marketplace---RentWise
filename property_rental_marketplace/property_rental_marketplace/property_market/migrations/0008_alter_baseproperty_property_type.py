# Generated by Django 4.2.2 on 2023-07-21 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property_market', '0007_building'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseproperty',
            name='property_type',
            field=models.CharField(choices=[('Apartment', 'Apartment'), ('Villa', 'Villa'), ('Office', 'Office'), ('Shop', 'Shop'), ('Building', 'Building')], max_length=20),
        ),
    ]
