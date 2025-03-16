from django import forms
from .models import Booking
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['event_name', 'booking_date', 'description', 'count']
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'event_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'count': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }
