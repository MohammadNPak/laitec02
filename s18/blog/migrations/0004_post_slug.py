# Generated by Django 4.0.6 on 2022-08-03 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='post_slug', max_length=250),
            preserve_default=False,
        ),
    ]
