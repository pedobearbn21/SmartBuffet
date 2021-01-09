# Generated by Django 3.1.4 on 2021-01-08 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TablestableInStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfMeat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tabeldailydate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_open_time', models.DateTimeField(auto_created=True)),
                ('status', models.CharField(choices=[('OPEN', 'OPEN'), ('CLOSE', 'CLOSE')], default='OPEN', max_length=5)),
                ('people_count', models.IntegerField()),
                ('table_close_time', models.DateTimeField(blank=True, null=True)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='table_of_dailytable', to='customer.tablestableinstore')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_time', models.DateTimeField(auto_created=True)),
                ('status', models.CharField(choices=[('ORDERED', 'ORDERED'), ('SERVED', 'SERVED')], default='ORDERED', max_length=7)),
                ('serve_time', models.DateTimeField(blank=True, null=True)),
                ('meats', models.ManyToManyField(to='customer.Meats')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_table', to='customer.tabeldailydate')),
            ],
        ),
        migrations.AddField(
            model_name='meats',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type_of_meat', to='customer.typeofmeat'),
        ),
    ]