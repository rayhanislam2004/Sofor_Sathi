from django import forms
from .models import LocationReview, RouteReview

class LocationReviewForm(forms.ModelForm):
    class Meta:
        model = LocationReview
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(attrs={'class': 'form-select'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class RouteReviewForm(forms.ModelForm):
    class Meta:
        model = RouteReview
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(attrs={'class': 'form-select'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

