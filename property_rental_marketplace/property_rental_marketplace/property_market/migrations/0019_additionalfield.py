# Generated by Django 4.2.2 on 2023-08-03 00:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property_market', '0018_apartment_garage'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=100)),
                ('field_type', models.CharField(choices=[('text', 'Text'), ('checkbox', 'Checkbox'), ('number', 'Number')], max_length=10)),
                ('property_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property_market.baseproperty')),
            ],
        ),
    ]