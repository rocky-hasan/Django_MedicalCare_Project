from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from .forms import Dealerform, EmployeeForm, CustomerForm, PurchaseForm
from django.http import Http404, request, HttpResponseRedirect
from .models import Dealerinfo, Employeeinfo, Customer, Medicineinfo, Purchase
from django.db import IntegrityError, models
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView


# Create your views here.
def home(request):
    return render(request, 'home.html')


def dealerform(request):
    context = {
        'add': True
    }
    return render(request, 'dealer.html', context)


# Class Based view

class DealerCreateView(CreateView):
    model = Dealerinfo
    template_name = 'dealer.html'
    context_object_name = 'dealer'
    form_class = Dealerform
    success_url = reverse_lazy('dealertable')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class DealerUpdateView(View):
    model = Dealerinfo
    form_class = Dealerform
    template_name = 'dealer.html'
    success_url = '/dealertable/'

    def form_valid(self, form):
        print(form.cleaned_data)
        print("form updated")
        return super().form_valid(form)

    def post(self, request, pk):
        try:
            Dealerinfo.objects.filter(pk=pk).update(
                dealer_name=request.POST['dealer_name'],
                address=request.POST['address'],
                phone_number=request.POST['phone_number'],
                email=request.POST['email']
            )
        except IntegrityError:
            return render(request, 'new.html')
        return redirect(self.success_url)


class Dealerformview(DetailView):
    model = Dealerinfo
    template_name = 'dealer.html'
    context_object_name = 'dealer'


def dealerformdelete(request, d_pk):
    dealer = Dealerinfo.objects.get(pk=d_pk)
    dealer.delete()
    return redirect('dealertable')


class Dealertable(ListView):
    model = Dealerinfo
    template_name = 'dealertable.html'
    context_object_name = 'dealer'


# _______Employee Info_________
def empform(request):
    context = {
        'add': True
    }
    return render(request, 'emp.html', context)


class EmpCreateView(CreateView):
    template_name = 'emp.html'
    context_object_name = 'emp'
    form_class = EmployeeForm
    success_url = reverse_lazy('emptable')


class EmpUpdateView(UpdateView):
    model = Employeeinfo
    template_name = 'emp.html'
    form_class = EmployeeForm
    context_object_name = 'emp'
    success_url = reverse_lazy('emptable')


'''class EmpUpdateView(View):
    model = Employeeinfo
    form_class = EmployeeForm
    template_name = 'emp.html'
    success_url = '/emptable/'

    def form_valid(self, form):
        print(form.cleaned_data)
        print("form updated")
        return super().form_valid(form)

    def post(self, request, pk):
        try:
            Employeeinfo.objects.filter(pk=pk).update(
                Emp_id=request.POST.get('Emp_id'),
                fname=request.POST.get('fname'),
                lname=request.POST.get('lname'),
                address=request.POST.get('address'),
                email=request.POST.get('email'),
                salary=request.POST.get('salary'),
                phone_number=request.POST.get('phone_number')
            )
        except IntegrityError:
            return render(request, 'new.html')
        return redirect(self.success_url)'''


class EmployeeFormView(DetailView):
    model = Employeeinfo
    template_name = 'emp.html'
    context_object_name = 'emp'


def empformdelete(request, pk):
    emp = Employeeinfo.objects.get(pk=pk)
    emp.delete()
    return redirect('emptable')


'''class EmployeeDeleteView(DeleteView):
    model = Employeeinfo
    template_name = 'emp.html'
    context_object_name = 'pk'
    success_url = reverse_lazy('emptable')'''


class EmployeeTableView(ListView):
    model = Employeeinfo
    template_name = 'emptable.html'
    context_object_name = 'emp'


# _______Customer Info______:
def custform(request):
    context = {
        'add': True
    }
    return render(request, 'cust.html', context)


class CustomerCreateView(CreateView):
    template_name = 'cust.html'
    context_object_name = 'cust'
    form_class = CustomerForm
    success_url = reverse_lazy('custtable')


class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'cust.html'
    form_class = CustomerForm
    context_object_name = 'cust'
    success_url = reverse_lazy('custtable')


def custformdelete(request, cust_pk):
    cust = get_object_or_404(Customer, pk=cust_pk)
    cust.delete()
    return redirect('custtable')


class CustomerListView(ListView):
    model = Customer
    template_name = 'custtable.html'
    context_object_name = 'cust'


class CustomerDetailsView(DetailView):
    model = Customer
    template_name = 'cust.html'
    context_object_name = 'cust'


# _____For Medicine_______:
from .forms import Medicineform


def medform(request):
    context = {
        'add': True
    }
    return render(request, 'med.html', context)


class MedDetailView(DetailView):
    model = Medicineinfo
    template_name = 'emp.html'
    context_object_name = 'emp'


class MedListView(ListView):
    model = Medicineinfo
    template_name = 'medtable.html'
    context_object_name = 'med'


class MedicineCreateView(CreateView):
    template_name = 'med.html'
    context_object_name = 'med'
    form_class = Medicineform
    success_url = reverse_lazy('medtable')

    def form_valid(self, form):
        response = super(MedicineCreateView, self).form_valid(form)

        dealer_name = form.cleaned_data['dname']

        dealer = Dealerinfo.objects.get(dname=dealer_name)

        return response


class MedUpdateView(UpdateView):
    model = Medicineinfo
    template_name = 'med.html'
    form_class = Medicineform
    success_url = reverse_lazy('medtable')


class MedDeleteView(DeleteView):
    model = Medicineinfo
    template_name = 'med_confirm_delete.html'
    success_url = reverse_lazy('medtable')


# _____for purchase_____:
def purchaseform(request):
    context = {
        'add': True
    }
    return render(request, 'purchase.html', context)


class PurchaseDetaileView(DetailView):
    model = Purchase
    template_name = 'purchase.html'
    context_object_name = 'purchase'


class PurchaseCreateView(CreateView):
    model = Purchase
    template_name = 'purchase.html'
    form_class = PurchaseForm
    success_url = reverse_lazy('purchasetable')

    def form_valid(self, form):
        print("Form is valid. Ready to save.")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form is invalid. Errors:")
        return super().form_invalid(form)


class PurchaseUpdateView(UpdateView):
    model = Purchase
    template_name = 'purchase.html'
    context_object_name = 'purchase'
    form_class = PurchaseForm
    success_url = reverse_lazy('purchasetable')


def purchaseformdelete(request, pur_pk):
    purchase = Purchase(pk=pur_pk)
    purchase.delete()
    return redirect('purchasetable')


class PurchaseListTable(ListView):
    model = Purchase
    context_object_name = 'purchase'
    template_name = 'purchasetable.html'
