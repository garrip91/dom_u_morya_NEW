from django.shortcuts import render, get_object_or_404

from .models import House

from orders.forms import OrderForm

from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import HousesFilterForm

from django.db.models import Q

from rest_framework import generics, viewsets
from .serializers import HouseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly

from rest_framework.authentication import TokenAuthentication



# Create your views here.
def houses_list(request):
    houses = House.objects.filter(active=True)
    # for house in houses:
        # print(house.name, house.price)
    form = HousesFilterForm(request.GET)
    if form.is_valid():
        if form.cleaned_data["ordering"]:
            houses = houses.order_by(form.cleaned_data["ordering"])
        if form.cleaned_data["min_price"]:
            houses = houses.filter(price__gte=form.cleaned_data["min_price"])
        if form.cleaned_data["max_price"]:
            houses = houses.filter(price__lte=form.cleaned_data["max_price"])
        if form.cleaned_data["query"]:
            houses = houses.filter(
                Q(description__icontains=form.cleaned_data["query"]) |
                Q(name__icontains=form.cleaned_data["query"]))
    return render(request, 'houses/houses_list.html', {'houses': houses, 'form': form})


def house_detail(request, house_id):
    house = get_object_or_404(House, id=house_id, active=True)
    form = OrderForm(request.POST or None, initial={'house': house})
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # {% url 'house' house_id=house.id %}
            url = reverse('house', kwargs={'house_id': house.id})
            return  HttpResponseRedirect(F'{url}?sent=1')
    return render(request, 'houses/house_detail.html', {
        'house': house,
        'form': form,
        'sent': "sent" in request.GET
    })


class HousesAPIListView(generics.ListCreateAPIView):

    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class HousesAPIUpdateView(generics.RetrieveUpdateAPIView):

    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = (TokenAuthentication,)


class HousesAPIDestroyView(generics.RetrieveDestroyAPIView):

    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = (IsAdminOrReadOnly,)


# class HousesAPIDetailView(generics.RetrieveUpdateDestroyAPIView):

    # queryset = House.objects.all()
    # serializer_class = HouseSerializer