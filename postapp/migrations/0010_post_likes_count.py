# Generated by Django 4.1 on 2022-09-23 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("postapp", "0009_alter_post_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="likes_count",
            field=models.IntegerField(default=0),
        ),
    ]
