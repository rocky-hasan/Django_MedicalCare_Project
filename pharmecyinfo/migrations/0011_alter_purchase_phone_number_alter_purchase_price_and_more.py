# Generated by Django 4.2.6 on 2023-10-17 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmecyinfo', '0010_rename_quanttity_purchase_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='total',
            field=models.IntegerField(),
        ),
    ]