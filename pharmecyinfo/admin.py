from django.contrib import admin
from .models import Dealerinfo,Customer,Purchase,Medicineinfo,Employeeinfo
# Register your models here.

@admin.register(Dealerinfo)
class DealerinfoAdmin(admin.ModelAdmin):
    list_display=['dealer_name','address','phone_number','email']


admin.site.register(Customer)
admin.site.register(Purchase)
admin.site.register(Medicineinfo)
admin.site.register(Employeeinfo)
