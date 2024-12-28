from django import forms

class VehicleForm(forms.Form):

    name=forms.CharField()

    brand=forms.CharField()

    price=forms.IntegerField()

    color=forms.CharField()

    fuel_type=forms.CharField()

    # specs=forms.CharField()

