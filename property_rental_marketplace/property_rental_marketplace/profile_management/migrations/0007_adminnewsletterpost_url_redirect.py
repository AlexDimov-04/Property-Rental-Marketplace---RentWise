# Generated by Django 4.2.2 on 2023-08-08 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_management', '0006_adminnewsletterpost_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminnewsletterpost',
            name='url_redirect',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
