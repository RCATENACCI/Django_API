
# Create your models here.
from django.db import models

class Trade(models.Model):
    asset = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.FloatField()
    trade_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.asset} - {self.quantity} @ {self.price}"
