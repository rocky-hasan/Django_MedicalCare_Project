from django import forms
from .models import Dealerinfo, Employeeinfo, Customer, Medicineinfo, Purchase


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['pname', 'fname', 'lname', 'phone_number', 'price', 'quantity']
        labels = {
            'pname': 'pname',
            'fname': 'fname',
            'lname': 'lname',
            'phone_number': 'phone_number',
            'price': 'price',
            'quantity': 'quantity'
        }


class Medicineform(forms.ModelForm):
    class Meta:
        model = Medicineinfo
        fields = ['m_id', 'mname', 'dname', 'desc', 'price', 'stock']
        labels = {
            'm_id': 'm_id',
            'mname': 'mname',
            'dname': 'dname',
            'desc': 'desc',
            'price': 'price',
            'stock': 'stock'

        }


class Dealerform(forms.ModelForm):
    class Meta:
        model = Dealerinfo
        fields = ['dealer_name', 'address', 'phone_number', 'email']
        labels = {
            'dealer_name': 'dealer_name',
            'address': 'address',
            'email': 'email',
            'phone_number': 'phone_number'

        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['fname', 'lname', 'address', 'email', 'phone_number']
        labels = {
            'fname': 'fname',
            'lname': 'lname',
            'address': 'address',
            'email': 'email',
            'phone_number': 'phone_number',
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
            'phone_number': 'phone_number',
        }
