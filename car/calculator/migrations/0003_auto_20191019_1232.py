# Generated by Django 2.2.6 on 2019-10-19 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_auto_20191016_1625'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currencychoice',
            old_name='currrency_code',
            new_name='currency_code',
        ),
        migrations.AddField(
            model_name='currencychoice',
            name='currency_rate',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=9),
        ),
    ]
