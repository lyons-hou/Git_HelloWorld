# Generated by Django 2.0.7 on 2018-07-31 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BusinessGroup', '0002_auto_20180731_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessgroup_info',
            name='Business_Group',
            field=models.CharField(max_length=20),
        ),
    ]
