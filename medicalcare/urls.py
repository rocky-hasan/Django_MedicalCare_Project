from django.contrib import admin
from django.urls import path
from pharmecyinfo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    # Dealer_________url_________:
    path('dealerform/', views.dealerform, name='dealerform'),

    path('dealerforminsert/', views.DealerCreateView.as_view(), name='dealerforminsert'),
    #path('dealerformupdate/<int:d_pk>/', views.dealerformupdate, name='dealerformupdate'),

    path('dealerformupdate/<int:id>/', views.DealerUpdateView.as_view(), name='dealerformupdate'),

    path('dealerformview/<int:pk>/', views.Dealerformview.as_view(), name='dealerformview'),
    path('dealerformdelete/<int:d_pk>/', views.dealerformdelete, name='dealerformdelete'),
    path('dealertable/', views.Dealertable.as_view(), name='dealertable'),

    #  Employee_______url_______:
    path('empform/', views.empform, name='empform'),
    #path('empforminsert/', views.empforminsert, name='empforminsert'),

    path('empforminsert/', views.EmpCreateView.as_view(), name='empforminsert'),

    path('empformupdate/<int:emp_pk>/', views.empformupdate,name='empformupdate'),
    path('empformdelete/<int:emp_pk>/', views.empformdelete, name='empformdelete'),
    path('empformview/<int:emp_pk>/',views.empformview, name='empformview'),
    path('emptable/', views.emptable, name='emptable'),

        #  Customer_______url_______:
    path('custform/', views.custform, name='custform'),
    path('custforminsert/', views.custforminsert, name='custforminsert'),
    path('custformupdate/<int:cust_pk>/',views.custformupdate,name='custformupdate'),
    path('custformdelete/<int:cust_pk>/', views.custformdelete, name='custformdelete'),
    path('custformview/<int:cust_pk>/',views.custformview, name='custformview'),
    path('custtable/', views.custtable, name='custtable'),

    #  Medicine_________url__________:
    path('medform/',views.medform, name='medform'),
    path('medformview/<int:med_pk>/',views.medformview, name='medformview'),
    path('medforminsert/', views.medforminsert, name='medforminsert'),
    path('medformupdate/<int:med_pk>/', views.medformupdate, name='medformupdate'),
    path('medformdelete/<int:med_pk>/',views.medformdelete, name='medformdelete'),
    path('medtable/',views.medtable, name='medtable'),

    #  Medicine_________url__________:
    path('purchaseform/',views.purchaseform, name='purchaseform'),
    path('purchaseformview/<int:pur_pk>/',views.purchaseformview, name='purchaseformview'),
    path('purchaseforminsert/', views.purchaseforminsert, name='purchaseforminsert'),
    path('purchaseformupdate/<int:pur_pk>/', views.purchaseformupdate, name='purchaseformupdate'),
    path('purchaseformdelete/<int:pur_pk>/',views.purchaseformdelete, name='purchaseformdelete'),
    path('purchasetable/',views.purchasetable, name='purchasetable'),
]
