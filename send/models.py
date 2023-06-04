from django.db import models
class Order(models.Model):
    #   order_id= models.AutoField(primary_key=True)
      message= models.CharField(max_length=5000)
      number=models.IntegerField(default=1)
# Create your models here.
