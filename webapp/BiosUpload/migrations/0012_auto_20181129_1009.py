# Generated by Django 2.1.3 on 2018-11-29 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BiosUpload', '0011_bios_package_senderinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bios_package',
            name='SenderInfo',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]