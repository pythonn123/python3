from django.urls import path
from . import views
urlpatterns = [
    path("", views.Home,name="Home"),
    # path("add/",views.addition,name="addition"),
    # path("Contact/",views.Contact,name="Contact"),
    # path("Details/",views.Details,name="Details"),
    # path("Thanks/",views.Thanks,name="Thanks"),
]