# Generated by Django 3.2.19 on 2023-07-26 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_alter_booking_booking_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_name',
            field=models.CharField(default='Ayla', max_length=40),
        ),
    ]
