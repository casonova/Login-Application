# Generated by Django 4.2.6 on 2023-11-14 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0006_alter_profile_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
