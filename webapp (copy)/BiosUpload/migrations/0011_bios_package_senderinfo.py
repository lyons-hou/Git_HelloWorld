# Generated by Django 2.1.3 on 2018-11-29 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BiosUpload', '0010_auto_20181008_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='bios_package',
            name='SenderInfo',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
