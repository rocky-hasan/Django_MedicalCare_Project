# Generated by Django 4.2.7 on 2023-11-17 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pharmecyinfo', '0012_alter_medicineinfo_dname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='total',
        ),
    ]