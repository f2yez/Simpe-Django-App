from django import forms
from .models import Client

class CreateClient(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('client_name', 'email', 'contact_name', 'address', 'phone_number')
        exclude = ()
