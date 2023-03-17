# Generated by Django 4.1.5 on 2023-03-17 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AirFlight_id', models.UUIDField()),
                ('AirCommpany', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AirLines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AirFlight_id', models.UUIDField()),
                ('AirCommpany', models.CharField(max_length=100)),
                ('DeparturePoint', models.CharField(max_length=100)),
                ('ArrivalPoint', models.CharField(max_length=100)),
                ('ForcedPoint', models.CharField(max_length=100, null=True)),
                ('AirFlight_departure_date', models.DateField(null=True)),
                ('AirFight_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('AirFlight_status', models.CharField(default='Straight', max_length=100)),
                ('AirFlight_type', models.CharField(default='Passenger', max_length=100)),
                ('Weather', models.CharField(default='Favorable', max_length=100)),
                ('Description_weather', models.CharField(default='Sunny', max_length=100)),
                ('Distance', models.DecimalField(decimal_places=100, max_digits=100)),
            ],
        ),
        migrations.CreateModel(
            name='ArrivalPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AirFlight_id', models.UUIDField()),
                ('ArrivalPoint_name', models.CharField(max_length=100)),
                ('ArrivalPoint_latitude', models.DecimalField(decimal_places=100, max_digits=100)),
                ('ArrivalPoint_longitude', models.DecimalField(decimal_places=100, max_digits=100)),
            ],
        ),
        migrations.CreateModel(
            name='DeparturePoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AirFlight_id', models.UUIDField()),
                ('DeparturePoint_name', models.CharField(max_length=100)),
                ('DeparturePoint_latitude', models.DecimalField(decimal_places=100, max_digits=100)),
                ('DeparturePoint_longitude', models.DecimalField(decimal_places=100, max_digits=100)),
            ],
        ),
        migrations.CreateModel(
            name='ForcedPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AirFlight_id', models.UUIDField()),
                ('ForcedPoint_name', models.CharField(max_length=100)),
                ('ForcedPoint_latitude', models.DecimalField(decimal_places=100, max_digits=100)),
                ('ForcedPoint_longitude', models.DecimalField(decimal_places=100, max_digits=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AirFlight_id', models.UUIDField()),
            ],
        ),
    ]
