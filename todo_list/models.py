from django.db import models
from django.utils import timezone

class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    time_est= models.DecimalField(max_digits=5, decimal_places=2, default=0)
    notes= models.CharField(max_length=10000, default="Notes")
    due_date = models.DateTimeField(default=timezone.now)
        
    def __str__(self):
        return self.item + ' | ' + str(self.completed)


