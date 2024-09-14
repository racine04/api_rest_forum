from django.db import models
from sujet.models import SujetModel
from base.models.helpers.named_date_time_model import NamedDateTimeModel


# Create your models here.

class MessageModel(NamedDateTimeModel):
    name = models.CharField(max_length=255, null=True)
    post = models.CharField(max_length=255, null=True)
    subject = models.ForeignKey(SujetModel, on_delete=models.CASCADE, related_name="sujet_message_id", null= True)

