# Generated by Django 2.0.7 on 2018-10-08 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BiosUpload', '0009_bios_package_ownername'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bios_package',
            name='PackageType',
            field=models.CharField(default='PKG', max_length=10),
        ),
    ]
