# Generated by Django 2.0.7 on 2018-07-31 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('BusinessGroup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductFamily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Family', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(max_length=30)),
                ('Business_Group', models.ManyToManyField(to='BusinessGroup.BusinessGroup_Info')),
                ('Product_Family', models.ManyToManyField(to='ProductInfo.ProductFamily')),
            ],
        ),
    ]
