from enum import Enum
from django.db import models
from django.utils import timezone

# Create your models here.
class OrderType(Enum) : 
    BUY = 'buy'
    SELL = 'sell'
    
class Brokerage(Enum):
    KRAKEN ="kraken"
    IB = "interactive_brokers"
    

class Order(models.Model):
    order_type = models.CharField(max_length=4, choices=[(tag.name, tag.value)for tag in OrderType])
    brokerages = models.CharField(max_length=50,choices=[(tag.name, tag.value)for tag in Brokerage])
    price = models.DecimalField(max_digits=20, decimal_places=10)
    quantity = models.DecimalField(max_digits=20, decimal_places=10)
    created_at = models.DateTimeField(default=timezone.now)
    filled_at = models.DateTimeField(blank=True, null=True)
    cancelled_at = models.DateTimeField(blank=True, null=True)