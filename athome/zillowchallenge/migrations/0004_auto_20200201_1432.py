# Generated by Django 3.0.2 on 2020-02-01 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zillowchallenge', '0003_auto_20200201_0412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='home_size',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='last_sold_price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='property_size',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='rent_price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='rentzestimate_amount',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='tax_value',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='zestimate_amount',
            field=models.FloatField(null=True),
        ),
    ]