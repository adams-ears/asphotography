# Generated by Django 3.1.6 on 2021-02-26 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0008_vouchercode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vouchercode',
            name='code',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
