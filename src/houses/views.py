from django.shortcuts import render, get_object_or_404

from .models import House

from orders.forms import OrderForm

from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import HousesFilterForm

from django.db.models import Q

from rest_framework import generics
from .serializers import HouseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict



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


# class HousesAPIView(generics.ListAPIView):

    # queryset = House.objects.all()
    # serializer_class = HouseSerializer
class HousesAPIView(APIView):

    def get(self, request):
        h = House.objects.all()
        return Response({'posts': HouseSerializer(h, many=True).data})

    def post(self, request):
        serializer = HouseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed!'})
        try:
            instance = House.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exists!'})
        serializer = HouseSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method DELETE not allowed!'})
        # здесь код для удаления записи с переданным pk
        return Response({'post': F'delete post {str(pk)}'})