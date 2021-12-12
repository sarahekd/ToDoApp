from django import forms
from .models import List

class ListForm(forms.ModelForm):
	class Meta:
		model = List
		fields= ["item", "due_date", "time_est", "completed", "notes"]
        

