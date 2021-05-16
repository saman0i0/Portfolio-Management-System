# Generated by Django 3.2.3 on 2021-05-15 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('units', models.IntegerField(max_length=10)),
                ('buy_price', models.FloatField()),
                ('curr_value', models.FloatField()),
                ('profit', models.FloatField()),
            ],
        ),
    ]