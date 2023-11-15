from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from .forms import Dealerform, EmployeeForm, CustomerForm
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


def medformview(request, med_pk):
    med = Medicineinfo.objects.get(pk=med_pk)
    context = {
        'med': med
    }
    return render(request, 'med.html', context)


class MedListView(ListView):
    model = Medicineinfo
    template_name = 'medtable.html'
    context_object_name = 'med'


'''def medforminsert(request):
    try:
        med = Medicineinfo()
        med.m_id = request.POST['mid']
        med.mname = request.POST['mname']
        med.dname = request.POST['dname']
        med.desc = request.POST['desc']
        med.stock = request.POST['stock']
        med.price = request.POST['price']
        med.save()
    except IntegrityError:
        return render(request, 'new.html')
    return redirect('medtable')'''


class MedicineCreateView(CreateView):
    template_name = 'med.html'
    context_object_name = 'med'
    form_class = Medicineform
    success_url = reverse_lazy('medtable')



'''def medformupdate(request, med_pk):
    try:
        med = get_object_or_404(Medicineinfo, pk=med_pk)
        med.m_id = request.POST['mid']
        med.mname = request.POST['mname']
        med.dname = request.POST['dname']
        med.desc = request.POST['desc']
        med.stock = request.POST['stock']
        med.price = request.POST['price']
        med.save()
    except IntegrityError:
        return render(request, 'new.html')
    return redirect('medtable')'''


class MedUpdateView(UpdateView):
    model = Medicineinfo
    template_name = 'med.html'
    form_class = Medicineform
    success_url = reverse_lazy('medtable')


'''def medformdelete(request, med_pk):
    med = get_object_or_404(Medicineinfo, pk=med_pk)
    med.delete()
    med.clean()
    return redirect('medtable')'''


class MedDeleteView(DeleteView):
    model = Medicineinfo
    template_name = 'med_confirm_delete.html'
    success_url = reverse_lazy('medtable')


'''def medtable(request):
    med = Medicineinfo.objects.all()
    context = {
        'med': med
    }
    return render(request, 'medtable.html', context)'''


# _____for purchase_____:
def purchaseform(request):
    context = {
        'add': True
    }
    return render(request, 'purchase.html', context)


def purchaseformview(request, pur_pk):
    purchase = Purchase.objects.get(pk=pur_pk)
    context = {
        'purchase': purchase
    }
    return render(request, 'purchase.html', context)


def purchaseforminsert(request):
    try:
        purchase = Purchase()
        purchase.pname = request.POST['pname']
        purchase.fname = request.POST['fname']
        purchase.lname = request.POST['lname']
        purchase.phone_number = request.POST['pno']
        purchase.price = request.POST['price']
        purchase.quantity = request.POST['qty']
        purchase.total = (int(purchase.price)) * (int(purchase.quantity))
        purchase.save()
    except IntegrityError:
        return render(request, 'new.html')
    return render(request, 'purchase.html')


def purchaseformupdate(request, pur_pk):
    try:
        purchase = get_object_or_404(Purchase, pk=pur_pk)
        purchase.pname = request.POST['pname']
        purchase.fname = request.POST['fname']
        purchase.lname = request.POST['lname']
        purchase.phone_number = request.POST['pno']
        purchase.price = request.POST['price']
        purchase.quantity = request.POST['qty']
        purchase.total = (int(purchase.price)) * (int(purchase.quantity))
        purchase.save()
    except IntegrityError:
        return render(request, 'new.html')
    return render(request, 'purchase.html')


def purchaseformdelete(request, pur_pk):
    purchase = Purchase(pk=pur_pk)
    purchase.delete()
    return redirect('purchasetable')


def purchasetable(request):
    purchase = Purchase.objects.all()
    context = {
        'purchase': purchase
    }
    return render(request, 'purchasetable.html', context)
