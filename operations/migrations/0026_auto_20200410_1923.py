# Generated by Django 3.0.4 on 2020-04-10 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0025_auto_20200410_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthcare',
            name='lat',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='healthcare',
            name='lng',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
    ]