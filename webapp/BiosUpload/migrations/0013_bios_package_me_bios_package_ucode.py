# Generated by Django 2.1.3 on 2020-07-26 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BiosUpload', '0012_auto_20181129_1009'),
    ]

    operations = [
        migrations.CreateModel(
            name='BIOS_Package_Me',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(max_length=30)),
                ('Version', models.CharField(max_length=20)),
                ('MeVersion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BIOS_Package_Ucode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(max_length=30)),
                ('Version', models.CharField(max_length=20)),
                ('UcodeVersion', models.TextField()),
            ],
        ),
    ]
