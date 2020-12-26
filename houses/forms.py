from django import forms

# Create your forms here:
class HousesFilterForm(forms.Form):
    min_price = forms.IntegerField(label="От", required=False)
    max_price = forms.IntegerField(label="до", required=False)
    ordering = forms.ChoiceField(label="Сортировка", required=False, choices=[
        ["name", "по алфавиту"],
        ["price", "дешёвые сверху"],
        ["-price", "дорогие сверху"]
    ])