from django.db import models

# Create your models here.

class ChartData(models.Model): 
    title = models.CharField(max_length=300) 
    
    def __str__(self):                                                                           
        return self.title
