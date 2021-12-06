from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here. ORM ==> Object Relational Mapper
class Snack(models.Model):
  name = models.CharField(max_length=30)
  purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  description = models.TextField(max_length=255)
  rating = models.IntegerField(default=0, validators=[
           MaxValueValidator(5),
           MinValueValidator(0)
        ])

  def __str__(self):
    return self.name  
