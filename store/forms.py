from django import forms
from .models import Product, Variation, ReviewRating

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields=['subject', 'review', 'rating']
