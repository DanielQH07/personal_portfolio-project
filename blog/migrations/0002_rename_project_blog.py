# Generated by Django 5.0.6 on 2024-07-12 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Project",
            new_name="Blog",
        ),
    ]
