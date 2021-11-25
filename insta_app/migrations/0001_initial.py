# Generated by Django 3.1.13 on 2021-11-20 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='insta_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insta_url', models.CharField(max_length=500)),
                ('picker_kind', models.CharField(choices=[('comments', 'Comments'), ('likes', 'Likes'), ('mentions', 'Mentions')], default='comments', max_length=8)),
                ('number_of_winers', models.DecimalField(decimal_places=0, max_digits=6)),
            ],
        ),
    ]