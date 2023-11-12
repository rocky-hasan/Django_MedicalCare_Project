from django import forms
from .models import Dealerinfo

class Dealerform(forms.ModelForm):
    class Meta:
        model = Dealerinfo
        fields = ['dealer_name','address','phone_number','email']
        labels={
        'dealer_name':'dname',
        'address': 'address',
        'email':'email',
        'phone_number':'pno'

    }