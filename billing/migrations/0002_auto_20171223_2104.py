# Generated by Django 2.0 on 2017-12-24 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='companyFirstFactureNumber',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='company',
            name='companyFirstFactureNumber1',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='company',
            name='companyFirstFactureNumber2',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='pdIvaState',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='productState',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='receivableaccount',
            name='receivableAccountInterest',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='setting',
            name='ACCURACY_VALUE',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='table',
            name='tableNumber',
            field=models.IntegerField(),
        ),
    ]