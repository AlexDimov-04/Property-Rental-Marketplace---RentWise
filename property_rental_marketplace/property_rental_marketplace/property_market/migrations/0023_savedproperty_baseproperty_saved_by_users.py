# Generated by Django 4.2.2 on 2023-08-04 12:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property_market', '0022_delete_additionalfield'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saved_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property_market.baseproperty')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='savedProperties', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='baseproperty',
            name='saved_by_users',
            field=models.ManyToManyField(related_name='saved_properties', through='property_market.SavedProperty', to=settings.AUTH_USER_MODEL),
        ),
    ]
