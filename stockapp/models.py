from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=30)
    companyico = models.ImageField(upload_to='company/', blank=True, null=True)


class StockInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    volume = models.IntegerField(help_text="거래량", blank=True, null=True)
    
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, related_name='info')
