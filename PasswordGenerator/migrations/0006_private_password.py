# Generated by Django 3.2 on 2021-04-30 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PasswordGenerator', '0005_remove_private_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='private',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
