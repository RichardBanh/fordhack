# Generated by Django 3.2.4 on 2021-07-15 02:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import fleetCommand.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FleetCommandModel',
            fields=[
                ('vehicleId', models.CharField(editable=False, max_length=255)),
                ('uuid', models.CharField(default=fleetCommand.models.hex_uuid, editable=False, max_length=32, primary_key=True, serialize=False, unique=True)),
                ('req_date', models.DateTimeField(auto_now_add=True)),
                ('ok_bySuper', models.BooleanField(default=False)),
                ('ok_byCustRep', models.BooleanField(default=False)),
                ('active_Req', models.BooleanField(default=True)),
                ('req', models.CharField(editable=False, max_length=255)),
                ('CustRep_Ok', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='CustRep_Ok', to=settings.AUTH_USER_MODEL)),
                ('Super_Ok', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Super_Ok', to=settings.AUTH_USER_MODEL)),
                ('initiated_byWho', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='initiated_byWho', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
