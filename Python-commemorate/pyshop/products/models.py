from django.db import models



class Product(models.Model):
    名字 = models.CharField(max_length=255)
    不知道 = models.FloatField()
    额 = models.IntegerField()
    网页 = models.CharField(max_length=2036)

class Off(models.Model):
    我 = models.CharField(max_length=10)
    爱 = models.CharField(max_length=255)
    黑 = models.FloatField()








