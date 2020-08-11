from django import forms
from products.models import review
        
class givereview(forms.ModelForm):
    comment= forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 20}))
    class Meta:
        model = review
        fields=[
            'score',
            'comment'
        ]
