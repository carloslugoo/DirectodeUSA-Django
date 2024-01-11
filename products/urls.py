from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('producto/<str:producto>', views.verproducto, name="verproducto")
]