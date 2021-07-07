from django.db import models
import uuid
# Create your models here.

def hex_uuid():
    return uuid.uuid4().hex

class accessKey(models.Model):
    uuid = models.CharField(
        max_length=32, default=hex_uuid, editable=False, unique=True, primary_key=True
    )
    access=models.CharField(max_length=800, blank=False, editable=True)
    timeCreated = models.DateTimeField(auto_now=True, editable=True)

    def __str__(self):
        return f'uuid: {self.uuid}.'
