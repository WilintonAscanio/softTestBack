# Generated by Django 4.1.9 on 2023-06-09 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soft_user_project', '0002_softuserproject_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='softuserproject',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
