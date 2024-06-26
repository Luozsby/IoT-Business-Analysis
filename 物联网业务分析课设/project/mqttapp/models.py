from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name=models.CharField(max_length=32)
    password=models.CharField(max_length=16)
    age=models.IntegerField()
    # data=models.IntegerField(null=True,blank=True)





class SensorData(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
# 增
# Deprtment.objects.create(title='销售部') 

# 删
# Deprtment.objects.filter(id=3).delete()
# Deprtment.objects.all()/delete()

# 查
# data_list=Deprtment.objects.all()

# 改
# Deprtment.objects.filter(id=2).update(age=999)
# Deprtment.objects.all().update(password=999)