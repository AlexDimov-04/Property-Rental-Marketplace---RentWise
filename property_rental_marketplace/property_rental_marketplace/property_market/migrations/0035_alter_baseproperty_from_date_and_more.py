# Generated by Django 4.2.2 on 2023-08-11 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property_market', '0034_alter_baseproperty_from_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseproperty',
            name='from_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='baseproperty',
            name='to_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
