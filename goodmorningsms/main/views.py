from django.shortcuts import render
from .models import Numbers
from .forms import NumberForm, TimezoneForm
from django.http import HttpResponseRedirect

# Create your views here.
#render used to render template

from django.http import HttpResponse


"""
def homepage(request): #always pass request  -- views.homepage

    return HttpResponse("Testing")
"""

def homepage(request):
    return render(request=request, template_name="main/home.html",
                    context={"numbers": Numbers.objects.all})

def get_number(request):
    print("hello")
    #if this is a POST request we need to process the form data
    if request.method == 'POST':
        #create a form instance and populate it with data from the request:
        num_form = NumberForm(request.POST, prefix="num_form")
        zone_form = TimezoneForm(request.POST,  prefix="zone_form")
        #check whether it's valid
        if num_form.is_valid() and zone_form.is_valid():
            num = num_form.cleaned_data['your_num']
            num_instance = Numbers.objects.create(phone=num)

            #process the data in form.cleaned_data as required
            #redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    #if a GET (or any other method) we'll create a blank form
    else:
        num_form = NumberForm(prefix="num_form")
        zone_form = TimezoneForm(prefix="zone_form")


        return render(request,"main/home.html",
                      {'num_form':num_form, 'zone_form':zone_form})