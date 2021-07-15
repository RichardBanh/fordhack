# Generated by Django 3.2.4 on 2021-07-15 01:49

from django.db import migrations, models
import systemFordK.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accessKey',
            fields=[
                ('uuid', models.CharField(default=systemFordK.models.hex_uuid, editable=False, max_length=32, primary_key=True, serialize=False, unique=True)),
                ('access', models.CharField(max_length=800)),
                ('timeCreated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
