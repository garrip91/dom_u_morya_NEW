from django import forms
from .models import Order

from houses.models import House



class OrderForm(forms.ModelForm):

    personal_data = forms.BooleanField(label="Я согласен на обработку персональных данных", required=True)
    house = forms.ModelChoiceField(queryset=House.objects.all(), widget=forms.HiddenInput)

    class Meta:
        model = Order
        fields = ['house', 'name', 'phone']