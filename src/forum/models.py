from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


# Create your models here.
class ForumModel(DateTimeModel):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
