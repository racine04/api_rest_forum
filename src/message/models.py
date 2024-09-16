from django.db import models
from sujet.models import SujetModel
from base.models.helpers.named_date_time_model import NamedDateTimeModel


# Create your models here.

class MessageModel(NamedDateTimeModel):
    post = models.CharField(max_length=255, null=True)
    subject = models.ForeignKey(SujetModel, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.post
