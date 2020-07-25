from django.urls import path
from cardsapp import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('thanks/', views.thanks, name = 'thanks'),
    path('about/', views.about, name='about'),
    path('donate/', views.donate, name='donate'),
    ]
