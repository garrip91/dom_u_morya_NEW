from django import forms



class HousesFilterForm(forms.Form):

    min_price = forms.IntegerField(label="От", required=False)
    max_price = forms.IntegerField(label="До", required=False)
    query = forms.CharField(label="Описание", required=False)
    ordering = forms.ChoiceField(label="Сортировка", required=False, choices=[
        ('name', "По алфавиту"),
        ('price', "Дешёвые сверху"),
        ('-price', "Дорогие сверху")
    ])