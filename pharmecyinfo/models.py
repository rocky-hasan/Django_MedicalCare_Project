from django.db import models


# Create your models here.

# -------for Dealer---------
class Dealerinfo(models.Model):
    dealer_name = models.CharField(max_length=30)
    address = models.CharField(max_length=200, default='N/A')
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True, default='example@example.com')

    def __str__(self):
        return self.email

    def __str__(self):
        return self.dealer_name


# _______for Employee______:
class Employeeinfo(models.Model):
    Emp_id = models.IntegerField(unique=True)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    salary = models.BigIntegerField()
    phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f"{self.Emp_id}: {self.fname} {self.lname}"


# ______for Customer_______:
class Customer(models.Model):
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.email


# _______for Medicine________:
class Medicineinfo(models.Model):
    m_id = models.IntegerField(unique=True)
    mname = models.CharField(max_length=15)
    dname = models.ForeignKey(Dealerinfo, on_delete=models.CASCADE)
    desc = models.CharField(max_length=100)
    price = models.BigIntegerField()
    stock = models.BigIntegerField()

    def __str__(self):
        return self.mname


# ______for Purchase_________:
class Purchase(models.Model):
    pname = models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    price = models.IntegerField()
    quantity = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return self.pname
