# Generated by Django 3.1.13 on 2021-11-25 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta_app', '0004_insta_ghost_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='insta_ghost_model',
            old_name='insta_url',
            new_name='insta_ID',
        ),
    ]
