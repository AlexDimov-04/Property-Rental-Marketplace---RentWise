# Generated by Django 4.2.2 on 2023-08-08 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_management', '0004_rename_title_adminnewsletterpost_newslwtter_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adminnewsletterpost',
            old_name='newslwtter_type',
            new_name='newsletter_type',
        ),
    ]
