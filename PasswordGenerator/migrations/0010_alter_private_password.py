# Generated by Django 3.2 on 2021-04-30 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PasswordGenerator', '0009_auto_20210501_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='private',
            name='password',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
