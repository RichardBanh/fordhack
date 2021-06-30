from django.db import models
import uuid
# Create your models here.
def hex_uuid():
    return uuid.uuid4().hex

class FordUptoDateModel(models.Model):
    uuid = models.CharField(
        max_length=32, default=hex_uuid, editable=False, unique=True
    )
    req_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.uuid