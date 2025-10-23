
from django import forms
from tourismapp.models import Location, Route

class LocationSubmissionForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['category', 'name', 'location', 'description', 'image']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

class RouteSubmissionForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['location', 'start_point', 'end_point', 'description']
        widgets = {
            'location': forms.Select(attrs={'class': 'form-select'}),
            'start_point': forms.TextInput(attrs={'class': 'form-control'}),
            'end_point': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
