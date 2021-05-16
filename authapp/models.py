from django.db import models

# Create your models here.

class Stock(models.Model):
    
    company_name = models.CharField(max_length=100)
    units = models.IntegerField()
    buy_price = models.FloatField()
    curr_value = models.FloatField()
    profit = models.FloatField()
    
    def __str__(self) -> str:
        return super().__str__()
        
    
