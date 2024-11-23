# Generated by Django 5.1.3 on 2024-11-22 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="full_name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
