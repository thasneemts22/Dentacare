from django.urls import path

from Dental_app import views


urlpatterns = [
    path('',views.index,name='index'),
    path('Doctor_Register',views.Doctor_Register,name='Doctor_Register'),
    path('login/',views.loginview,name='login'),
    path('doctor',views.doctorindex,name='doctor'),
    path('reg/',views.reg,name='reg'),
    path('app_booking',views.app_booking,name='app_booking'),
    path('prescription/<int:id>',views.prescription,name='prescription'),

]