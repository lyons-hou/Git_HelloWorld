# Generated by Django 2.0.7 on 2018-09-18 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BiosUpload', '0006_auto_20180917_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='bios_package',
            name='CustomerName',
            field=models.CharField(default='ADLINK', max_length=30),
        ),
    ]
