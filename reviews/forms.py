from django import forms
from .models import PerfumeReview

class ReviewForm(forms.ModelForm):
    class Meta:
        model = PerfumeReview
        
        fields = ['perfume_name', 'content']
        
        labels = {
            'perfume_name': 'お気に入りの香水',
            'content': '香りの感想（レビュー）',
        }