from django import forms
from .models import Dealerinfo, Employeeinfo


class Dealerform(forms.ModelForm):
    class Meta:
        model = Dealerinfo
        fields = ['dealer_name', 'address', 'phone_number', 'email']
        labels = {
            'dealer_name': 'dname',
            'address': 'address',
            'email': 'email',
            'phone_number': 'pno'

        }


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employeeinfo
        fields = ['Emp_id', 'fname', 'lname', 'address', 'email', 'salary', 'phone_number']
        labels = {
            'Emp_id': 'eid',
            'fname': 'fname',
            'lname': 'lname',
            'address': 'address',
            'email': 'email',
            'salary': 'salary',
            'phone_number': 'pno',
        }
