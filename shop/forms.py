from django import forms
from shop.models import Vehicle

# class VehicleForm(forms.Form):

#     name=forms.CharField()

#     brand=forms.CharField()

#     price=forms.IntegerField()

#     color=forms.CharField()

#     fuel_type=forms.CharField()

#     # specs=forms.CharField()

#     image=forms.ImageField()
class VehicleForm(forms.ModelForm):

    class Meta:

        model=Vehicle

        fields="__all__"

        widgets={
            "name":forms.TextInput(attrs={"class":"form-control mb-3"}),
            "brand":forms.TextInput(attrs={"class":"form-control mb-3"}),
            "color":forms.TextInput(attrs={"class":"form-control mb-3"}),
            "price":forms.NumberInput(attrs={"class":"form-control mb-3"}),
            "fuel_type":forms.TextInput(attrs={"class":"form-control mb-3"}),
            "image":forms.FileInput(attrs={"class":"form-control mb-3"})
        }
