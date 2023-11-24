from django.urls import path
from . import views
app_name = 'myapp'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('<int:pk>/', views.home_detailpage, name='home_detail'),
    path('about/', views.aboutpage, name='about'),
    path('services/', views.servicespage, name='services'),
    path('login/', views.loginpage, name='login'),
    path('contact/', views.contactpage, name='contact'),
    path('home/<str:slug>', views.home),
]
