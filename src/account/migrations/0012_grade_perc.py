# Generated by Django 4.2.4 on 2023-11-26 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_lettergrades'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='perc',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
    ]
