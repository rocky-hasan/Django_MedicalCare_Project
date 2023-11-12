# Generated by Django 4.2.6 on 2023-10-15 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmecyinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealerinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealer_name', models.CharField(max_length=30)),
                ('address', models.CharField(default='N/A', max_length=200)),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(default='example@example.com', max_length=254, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Dealer',
        ),
    ]