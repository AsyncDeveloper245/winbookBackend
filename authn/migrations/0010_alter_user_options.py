# Generated by Django 4.1 on 2022-09-23 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authn", "0009_user_blocked_users"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={"ordering": ("pk",)},
        ),
    ]
