# sendemail/forms.py
from django import forms

class ContactForm(forms.Form):
    first_name=forms.CharField( max_length=50, required=False)
    last_name=forms.CharField( max_length=50, required=False)
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)