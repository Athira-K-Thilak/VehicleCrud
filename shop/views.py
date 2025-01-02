from django.shortcuts import render,redirect
from django.views.generic import View
from shop.forms import VehicleForm
from shop.models import Vehicle

from django.db.models import Q
# Create your views here.

class VehicleCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=VehicleForm()

        return render(request,'vehicle_add.html',{'form':form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form__instance=VehicleForm(form_data,files=request.FILES)

        if form__instance.is_valid():

            data=form__instance.cleaned_data

            print(data)#{'name': 'vehicle1', 'brand': 'brand', 'price': 1223333, 'color': 'red', 'fuel_type': 'petrol'}

            Vehicle.objects.create(
                name=data.get("name"),
                brand=data.get("brand"),
                price=data.get("price"),
                color=data.get("color"),
                fuel_type=data.get("fuel_type"),
                image=data.get("image")
            )
            
            return redirect('vehicle-list')

        return render(request,'vehicle_add.html',{'form':form__instance})    

class VehicleListView(View):

    def get(self,request,*args,**kwargs):

        search_text=request.GET.get("search")

        print(search_text)

        qs=Vehicle.objects.all()

        if search_text:

            qs=qs.filter(Q(name__contains=search_text)|Q(brand__contains=search_text))

        return render(request,'vehicle_list.html',{'data':qs})
    
class VehicleDetailView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get('pk')

        qs=Vehicle.objects.get(id=id) 

        return render(request,'vehicle_detail.html',{'data':qs})   
    
class VehicleDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Vehicle.objects.get(id=id).delete()

        return redirect('vehicle-list')
    
class VehicleUpdateView(View):

    def get(self,request,*args,**kwargs):
        
        id=kwargs.get('pk')

        vehicle_obj=Vehicle.objects.get(id=id)

        vehicle_dictionary={
            'name':vehicle_obj.name,
            'brand':vehicle_obj.brand,
            'color':vehicle_obj.color,
            'price':vehicle_obj.price,
            'fuel_type':vehicle_obj.fuel_type
            
        }

        form_instance=VehicleForm(initial=vehicle_dictionary)

        return render(request,'vehicle_edit.html',{'form':form_instance})   

    def post(self,request,*args,**kwargs):

        form_data=request.POST


        form_instance=VehicleForm(form_data)

        id=kwargs.get('pk')

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Vehicle.objects.filter(id=id).update(**data)
           
            return redirect('vehicle-list')

        return render(request,'vehicle_edit.html',{'form':form_instance}) 





