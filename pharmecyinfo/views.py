from typing import Any
from django.shortcuts import render,get_object_or_404, redirect
from .forms import Dealerform
from django.http import Http404
from .models import Dealerinfo,Employeeinfo,Customer,Medicineinfo,Purchase
from django.db import IntegrityError, models
from django.views.generic import ListView, DetailView, DeleteView   #{ Showing data }


# Create your views here.
def home(request):
    return render(request, 'home.html')

def dealerform(request):
    context={
        'add': True
    }
    return render(request, 'dealer.html', context)

def dealerforminsert(request):
    try:
        dealer = Dealerinfo()
        dealer.dealer_name = request.POST['dname']
        dealer.address = request.POST['address']
        dealer.phone_number = request.POST['pno']
        dealer.email = request.POST['email']
        dealer.save()
    except IntegrityError:
        return render(request, "new.html")
    return redirect('dealertable')

def dealerformupdate(request, d_pk):
    try:
        dealer = get_object_or_404(Dealerinfo, pk=d_pk)
        dealer.dealer_name = request.POST['dname']
        dealer.address = request.POST['address']
        dealer.phone_number = request.POST['pno']
        dealer.email = request.POST['email']
        dealer.save()
    except IntegrityError:
        return render(request, 'new.html')
    return redirect('dealertable')

# Class Based view
class Dealerformview(DetailView):
    model = Dealerinfo
    template_name = 'dealer.html'
    context_object_name = 'dealer'


def dealerformdelete(request, d_pk):
    dealer = Dealerinfo.objects.get(pk=d_pk)
    dealer.delete()
    return redirect('dealertable')


class Dealertable(ListView):
    model =Dealerinfo
    template_name = 'dealertable.html'
    context_object_name = 'dealer'

#_______Employee Info_________
def empform(request):
    context={
        'add':True
    }
    return render(request, 'emp.html',context)

def empforminsert(request):
    try:
        emp = Employeeinfo()
        emp.Emp_id = request.POST['eid']
        emp.fname = request.POST['fname']
        emp.lname = request.POST['lname']
        emp.address = request.POST['address']
        emp.email = request.POST['email']
        emp.salary = request.POST['sal']
        emp.phone_number = request.POST['pno']
        emp.save()
    except IntegrityError:
        return render(request, 'new.html')
    return redirect('empforminsert')

def empformupdate(request, emp_pk):
    try:
        emp = get_object_or_404(Employeeinfo, pk=emp_pk)
        emp.Emp_id = request.POST['eid']
        emp.fname = request.POST['fname']
        emp.lname = request.POST['lname']
        emp.address = request.POST['address']
        emp.email = request.POST['email']
        emp.salary = request.POST['sal']
        emp.phone_number = request.POST['pno']
        emp.save()
    except IntegrityError:
        return render(request, 'new.html')
    return redirect('emptable')    

def empformdelete(request,emp_pk):
    emp = Employeeinfo.objects.get(pk=emp_pk)
    emp.delete()
    return redirect('emptable')
def emptable(request):
    emp= Employeeinfo.objects.all()
    context={
        'emp':emp
    }
    return render(request, 'emptable.html',context)

def empformview(request, emp_pk):
    emp = Employeeinfo.objects.get(pk=emp_pk)
    context={
        'emp':emp
    }
    return render(request,'emp.html',context)

#_______Customer Info______:
def custform(request):
    context={
        'add':True
    }
    return render(request, 'cust.html', context)
def custforminsert(request):
    try:
        cust= Customer()
        cust.fname=request.POST['fname']
        cust.lname = request.POST['lname']
        cust.address = request.POST['address']
        cust.phone_number = request.POST['pno']
        cust.email = request.POST['email']
        cust.save()
    except IntegrityError:
        return render(request, 'new.html')
    return redirect('custtable')

def custformupdate(request, cust_pk):
    try:
        cust=get_object_or_404(Customer, pk=cust_pk)
        cust.fname=request.POST['fname']
        cust.lname = request.POST['lname']
        cust.address = request.POST['address']
        cust.phone_number = request.POST['pno']
        cust.email = request.POST['email']
        cust.save()
    except IntegrityError:
        return render(request, 'new.html')
    return redirect('custtable')
def custformdelete(request, cust_pk):
    cust=get_object_or_404(Customer, pk=cust_pk)
    cust.delete()
    return redirect('custtable')
def custtable(request):
    cust = Customer.objects.all()
    context={
        'cust':cust
    }
    return render(request, 'custtable.html',context)
def custformview(request, cust_pk):
    cust = Customer.objects.get(pk=cust_pk)
    context={
        'cust':cust
    }
    return render(request,'cust.html',context)

#_____For Medicine_______:
def medform(request):
    context={
        'add':True
    }
    return render(request, 'med.html', context)

def medformview(request,med_pk):
    med= Medicineinfo.objects.get(pk=med_pk)
    context={
        'med':med
    }
    return render(request, 'med.html',context)

def medforminsert(request):
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
    return redirect('medtable')

def medformupdate(request, med_pk):
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
    return redirect('medtable')

def medformdelete(request,med_pk):
    med=get_object_or_404(Medicineinfo, pk=med_pk)
    med.delete()
    med.clean()
    return redirect('medtable')

def medtable(request):
    med = Medicineinfo.objects.all()
    context={
        'med':med
    }
    return render(request, 'medtable.html',context)

#_____for purchase_____:
def purchaseform(request):
    context={
        'add':True
    }
    return render(request, 'purchase.html', context)

def purchaseformview(request, pur_pk):
    purchase=Purchase.objects.get(pk=pur_pk)
    context={
        'purchase':purchase
    }
    return render(request, 'purchase.html',context)

def purchaseforminsert(request):
    try:
        purchase=Purchase()
        purchase.pname=request.POST['pname']
        purchase.fname=request.POST['fname']
        purchase.lname=request.POST['lname']
        purchase.phone_number=request.POST['pno']
        purchase.price=request.POST['price']
        purchase.quantity=request.POST['qty']
        purchase.total=(int(purchase.price))*(int(purchase.quantity))
        purchase.save()
    except IntegrityError:
        return render(request,'new.html')
    return render(request, 'purchase.html')

def purchaseformupdate(request, pur_pk):
    try:
        purchase=get_object_or_404(Purchase, pk=pur_pk)
        purchase.pname=request.POST['pname']
        purchase.fname=request.POST['fname']
        purchase.lname=request.POST['lname']
        purchase.phone_number=request.POST['pno']
        purchase.price=request.POST['price']
        purchase.quantity=request.POST['qty']
        purchase.total=(int(purchase.price))*(int(purchase.quantity))
        purchase.save()
    except IntegrityError:
        return render(request,'new.html')
    return render(request, 'purchase.html')
def purchaseformdelete(request,pur_pk):
    purchase=Purchase(pk=pur_pk)
    purchase.delete()
    return redirect('purchasetable')

def purchasetable(request):
    purchase= Purchase.objects.all()
    context={
        'purchase':purchase
    }
    return render(request, 'purchasetable.html', context)






