# Generated by Django 5.1.6 on 2025-02-28 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0004_alter_booking_bid_alter_payment_pid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='bid',
            field=models.CharField(default='cf50dfffdd', editable=False, max_length=13, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='payment',
            name='pid',
            field=models.CharField(default='5fc0df0e80', editable=False, max_length=13, primary_key=True, serialize=False),
        ),
    ]
