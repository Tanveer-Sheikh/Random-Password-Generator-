# Generated by Django 3.2 on 2021-04-30 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PasswordGenerator', '0006_private_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='private',
            name='password',
            field=models.CharField(max_length=32, null=True, verbose_name='password'),
        ),
    ]
