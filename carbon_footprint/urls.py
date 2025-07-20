from django.urls import path
from . import views

urlpatterns = [
    path('',views.registerpage),
    path('mainpage/',views.mainpage),
    path('usersignup/',views.registerpage),
    path('userlogin/',views.userlog),
    path('adminlog/',views.adminlog),
    path('adminloginoptions/',views.adminlogoptions),
    path('pending/',views.pending),
    path('approved/',views.approved),
    path('approve/<int:id>/',views.approve),
    path('operations/',views.operations),
    path('edit/<int:id>/',views.edit),
    path('delete/<int:id>/',views.delete)
]