# Generated by Django 2.0.7 on 2018-09-19 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BiosUpload', '0007_bios_package_customername'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bios_package',
            name='FileNameRef',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
