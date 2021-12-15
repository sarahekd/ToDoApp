from django.db import models
from django.utils import timezone

class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True)
    time_est= models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    notes= models.CharField(max_length=10000, default="Notes", blank=True)
    due_date = models.DateTimeField(null=True, default=timezone.now, blank=True)
    priority = models.CharField(max_length=200, default="Priority", blank=True) #eventually I'll switch this to a drop down with choices
        
    def __str__(self):
        return self.item + ' | ' + str(self.completed)


