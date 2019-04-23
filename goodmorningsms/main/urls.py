













from . import views
from django.urls import path

app_name = "main"

urlpatterns = [
    #When no url is entered, go to the homepage view called homepage
    path("",views.get_number, name="homepage")


]