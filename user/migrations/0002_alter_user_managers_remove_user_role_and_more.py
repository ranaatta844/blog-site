# Generated by Django 4.2.2 on 2023-06-10 09:53

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[
                ("objects", user.models.BlogUserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name="user",
            name="role",
        ),
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                max_length=254, unique=True, verbose_name="email address"
            ),
        ),
    ]
