# Generated by Django 4.2.2 on 2023-08-07 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterFollower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]