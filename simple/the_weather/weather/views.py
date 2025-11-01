from django.shortcuts import render, redirect
from django.views import View
import requests
import logging
from  .models import City
from .forms import CityForm

logger = logging.getLogger(__name__)
''' 
# Create your views here.
def index(request):
     if request.method == 'POST': # only tru if the form submitted
         form = CityForm(request.POST) # add actual request data to the form for processing 
         form.save() # will validate and save if validate
     form = CityForm()
     weather_data = []
     cities = City.objects.all() # returns all the cities in the database
     for idx, city in  enumerate(cities):
          
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=YOUR_APP_KEY'
        #city_weather  =requests.get(url.format(city)).json() # request the API data and convert the JSON to Python data types
        weather = {
            'city' : city,
            'temperature' :"21c->" + str(idx),
            'description' : "description->" + str(idx),
            'icon' : "icon->" + str(idx),
        }
        logger.info(weather)
        weather_data.append(weather)
     

     context = {'weather_data': weather_data, 'form':form}
     
     return render(request, 'weather/index.html', context) # return the index.html template
'''

class IndexView(View):
    form_class = CityForm
    template_name = 'weather/index.html'

    def get(self, request, *args, **kwargs):
        form = CityForm()
        weather_data = []
        cities = City.objects.all() # returns all the cities in the database
        for idx, city in  enumerate(cities):
            
            url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=YOUR_APP_KEY'
            #city_weather  =requests.get(url.format(city)).json() # request the API data and convert the JSON to Python data types
            weather = {
                'city' : city,
                'temperature' :"21c->" + str(idx),
                'description' : "description->" + str(idx),
                'icon' : "icon->" + str(idx),
            }
            logger.info(weather)
            weather_data.append(weather)
        

        context = {'weather_data': weather_data, 'form':form}
        
        return render(request, 'weather/index.html', context) # return the index.html template
    
    
    def post(self, request, *args, **kwargs):
         form = self.form_class(request.POST)

         if form.is_valid():
            form.save() # will validate and save if validate
         

         return redirect('/')
         

