from django import forms
from .models import Venue, Review, Booking

class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['name', 'description', 'category', 'capacity', 'price_per_hour', 'address', 'image']

    def clean_capacity(self):
        capacity = self.cleaned_data.get('capacity')
        if capacity <= 0:
            raise forms.ValidationError("Capacity must be a positive number.")
        return capacity

    def clean_price_per_hour(self):
        price = self.cleaned_data.get('price_per_hour')
        if price <= 0:
            raise forms.ValidationError("Price must be a positive number.")
        return price

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['start_time']

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)