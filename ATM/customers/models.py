from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    balance = models.FloatField()
    allowed_amount =  models.FloatField()
    neg_allowed =  models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.name

class Card(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=20)
    expire_date = models.DateField(null=False)
    password = models.CharField(max_length=100)
    card_status = models.IntegerField(choices=((0,0),(1,1)))
    attempts =models.IntegerField(default=3)

    def __str__(self) :
        return str(self.customer.id)