from django.shortcuts import render

from .models import House



# Create your views here.
def houses_list(request):
    houses = House.objects.all()
    for house in houses:
        print(house.name, house.price)
    return render(request, 'houses/houses_list.html', {'houses': houses})