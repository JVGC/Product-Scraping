""" Habits App URLs """
from django.urls import path

from . import views

# this name "urlpatterns" cannot be change to snake case
urlpatterns = [
    path("<int:code>", views.GetProductByCode.as_view(), name="GetProductByCode"),
    path("", views.ListProducts.as_view(), name="ListProducts"),
]
