from django.shortcuts import render
from django.views.generic import View
from shop.forms import VehicleForm
from shop.models import Vehicle
# Create your views here.

class VehicleCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=VehicleForm()

        return render(request,'vehicle_add.html',{'form':form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form__instance=VehicleForm(form_data)

        if form__instance.is_valid():

            data=form__instance.cleaned_data

            print(data)#{'name': 'vehicle1', 'brand': 'brand', 'price': 1223333, 'color': 'red', 'fuel_type': 'petrol'}

            Vehicle.objects.create(
                name=data.get("name"),
                brand=data.get("brand"),
                price=data.get("price"),
                color=data.get("color"),
                fuel_type=data.get("fuel_type")
            )

        return render(request,'vehicle_add.html',{'form':form__instance})    

