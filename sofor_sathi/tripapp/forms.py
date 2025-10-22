from django import forms
from .models import Trip, Budget


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        exclude = ['trip']
        widgets = {
            'transport_cost': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 5000'}),
            'food_cost': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 3000'}),
            'hotel_cost': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 4000'}),
            'other_cost': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 1000'}),
        }
