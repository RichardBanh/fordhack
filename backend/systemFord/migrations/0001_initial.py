# Generated by Django 3.2.4 on 2021-06-30 22:20

from django.db import migrations, models
import systemFord.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FordUptoDateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(default=systemFord.models.hex_uuid, editable=False, max_length=32, unique=True)),
                ('req_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
