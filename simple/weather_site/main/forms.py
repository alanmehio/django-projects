from django import forms


class CityForm(forms.Form):
    city = forms.CharField()


    #def __str__(self) -> str:
    #   return self.city

