# Generated by Django 2.0.7 on 2018-09-19 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BiosUpload', '0008_auto_20180919_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='bios_package',
            name='OwnerName',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
