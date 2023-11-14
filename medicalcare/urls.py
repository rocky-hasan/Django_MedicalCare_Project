from django.contrib import admin
from django.urls import path
from pharmecyinfo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    # Dealer_________url_________:
    path('dealerform/', views.dealerform, name='dealerform'),

    path('dealerforminsert/', views.DealerCreateView.as_view(), name='dealerforminsert'),
    path('dealerformupdate/<int:pk>/', views.DealerUpdateView.as_view(), name='dealerformupdate'),
    path('dealerformview/<int:pk>/', views.Dealerformview.as_view(), name='dealerformview'),
    path('dealerformdelete/<int:d_pk>/', views.dealerformdelete, name='dealerformdelete'),

    path('dealertable/', views.Dealertable.as_view(), name='dealertable'),

    #  Employee_______url_______:
    path('empform/', views.empform, name='empform'),
    path('empforminsert/', views.EmpCreateView.as_view(), name='empforminsert'),
    path('empformupdate/<int:pk>/', views.EmpUpdateView.as_view(),name='empformupdate'),
    path('empformview/<int:pk>/', views.EmployeeFormView.as_view(), name='empformview'),
    path('emptable/', views.EmployeeTableView.as_view(), name='emptable'),
    path('empformdelete/<int:pk>/', views.empformdelete, name='empformdelete'),


        #  Customer_______url_______:
    path('custform/', views.custform, name='custform'),
    path('custforminsert/', views.CustomerCreateView.as_view(), name='custforminsert'),

    #path('custformupdate/<int:cust_pk>/',views.custformupdate,name='custformupdate'),
    path('custformupdate/<int:pk>/', views.CustomerUpdateView.as_view(), name='custformupdate'),




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
