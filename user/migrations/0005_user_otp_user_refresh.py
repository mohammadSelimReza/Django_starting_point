# Generated by Django 5.1.3 on 2024-11-22 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0004_alter_user_full_name_alter_user_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="otp",
            field=models.CharField(
                blank=True, default="123456", max_length=6, null=True
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="refresh",
            field=models.CharField(blank=True, default="x", max_length=255, null=True),
        ),
    ]
