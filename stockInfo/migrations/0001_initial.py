# Generated by Django 2.0.5 on 2019-10-16 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stockInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexchange', models.CharField(max_length=10)),
                ('scode', models.CharField(max_length=40)),
                ('scompany_name', models.CharField(max_length=40)),
                ('sindustry', models.CharField(max_length=40)),
                ('spe_ttm', models.FloatField(max_length=40)),
                ('spb', models.FloatField(max_length=40)),
                ('sdividend_yield', models.FloatField(max_length=40)),
                ('sstock_prices', models.FloatField(max_length=40)),
                ('spb_ten_year', models.FloatField(max_length=40)),
            ],
        ),
    ]