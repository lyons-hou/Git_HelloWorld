# Generated by Django 2.0.7 on 2018-09-17 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BiosUpload', '0004_bios_package_biostype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bios_package',
            name='FileNameRef',
            field=models.CharField(max_length=30),
        ),
    ]
