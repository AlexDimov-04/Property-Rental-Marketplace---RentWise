# Generated by Django 4.2.2 on 2023-08-08 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_management', '0003_adminnewsletterpost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adminnewsletterpost',
            old_name='title',
            new_name='newslwtter_type',
        ),
    ]
