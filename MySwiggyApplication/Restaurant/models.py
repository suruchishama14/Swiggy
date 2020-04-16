from django.db import models
from adminpage.models import AreaModel
from adminpage.models import RestaurantTypeModel


class RestaurantModel(models.Model):
    restro_id = models.AutoField(primary_key=True)
    restro_name = models.CharField(unique=True,max_length=30)
    restro_contact = models.IntegerField(unique=True)
    restro_email = models.EmailField(max_length=100,unique=True)
    restro_area = models.ForeignKey(AreaModel,on_delete=models.CASCADE)
    restro_type = models.ForeignKey(RestaurantTypeModel,on_delete=models.CASCADE)
    restro_password = models.CharField(max_length=30)
    restro_otp = models.IntegerField()
    restro_status = models.CharField(max_length=30,default=False)

class Food(models.Model):
    id = models.IntegerField(primary_key=True)
    restro_id = models.ForeignKey(RestaurantModel, on_delete=models.CASCADE)
    food_name=models.CharField(max_length=30)
    def __str__(self):
        return self.restro_id