# Generated by Django 3.2.4 on 2021-07-03 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('vehicleId', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('make', models.CharField(max_length=30)),
                ('modelName', models.CharField(max_length=30)),
                ('modelYear', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=50)),
                ('nickName', models.CharField(max_length=255)),
                ('modemEnabled', models.BooleanField()),
                ('vehicleAuthorizationIndicator', models.PositiveIntegerField()),
                ('serviceCompatible', models.BooleanField()),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
