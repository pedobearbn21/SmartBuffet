# Generated by Django 3.1.4 on 2020-12-23 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20201223_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='meat',
            field=models.ManyToManyField(blank=True, related_name='meat_list', to='customer.meat'),
        ),
    ]