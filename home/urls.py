from django.urls import path
from . import views
urlpatterns = [
    path( '', views.home, name='home' ),
    path('about/',views.about, name='about'),
    path('contact/', views.contact, name="contact"),
    path('animals/', views.animal_list, name='animal_list'),
    path('animal/<int:pk>/', views.animal_detail, name='animal_detail'),
]
