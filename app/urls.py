from django.urls import path
from.import views

urlpatterns = [
    path('',views.method),
    path('addshow', views.method1),
    path('shows/<id>',views.method3),
    path('del/<num>',views.delet),
    path('shows',views.method4),
    path('shows/<id1>/edit',views.method5),
    path('addedit/<num1>',views.method6),
    
]