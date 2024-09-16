from django.db import models
from forum.models import ForumModel
from base.models.helpers.date_time_model import DateTimeModel


# Create your models here.
class SujetModel(DateTimeModel):
    forum = models.ForeignKey(ForumModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
