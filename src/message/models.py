from django.db import models
from sujet.models import SujetModel
from base.models.helpers.date_time_model import DateTimeModel


# Create your models here.

class MessageModel(DateTimeModel):
    subject = models.ForeignKey(SujetModel, on_delete=models.CASCADE)
    post = models.CharField(max_length=255)

    def __str__(self):
        return self.post
