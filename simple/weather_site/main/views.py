from django.shortcuts import render,redirect
from django.urls import reverse
from django.views import View
from django.contrib import messages
from . forms import CityForm
import logging


# Create your views here.
logger = logging.getLogger(__name__)
class IndexView(View):
    form_class = CityForm
    template_name = 'main/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
     
    def post(self, request, *args, **kwargs):
        form  = self.form_class(request.POST)
        if form.is_valid():
            city = form.cleaned_data.get('city')
            logger.info(f'City is {city}')
            # call the weather API and if there is no error etc.. 
            weather =  {
                "country_code": "SE",
                "coordinate" : "234234.555",
                "temp": "23",
                "pressure": "pressureOK",
                "humidity":"humidityOK",   
            }
            return render(request, self.template_name, weather)
        else:
            logger.info('Form is not valid ....')
            messages.info(request, "Could not find the city to search in case call does not get a result to remove site ")
            return render(request, self.template_name)

'''
def index(request):
    if(request.method == 'POST'):
       form = CityForm(request.POST)
       if form.is_valid():
           city = form.cleaned_data.get('city')
           # do the call and populate the weather as below 
           weather =  {
            "country_code": "SE",
            "coordinate" : "234234.555",
            "temp": "23",
            "pressure": "pressureOK",
            "humidity":"humidityOK",
            }
           return render(request, 'main/index.html', weather)
      

    return render(request, 'main/index.html')
'''