from django.shortcuts import render, redirect
from app import models
from app import forms



def list(request):
    country_list = models.Countries.objects.order_by('name')
    country_stats = models.CountryStats.objects.filter(year = 2018)
    return render(request,'app/list.html', {'countries': country_list, 'stats': country_stats})

def list_region(request, r_id):
    country_list = models.Countries.objects.order_by('name')
    region_list = models.Regions.objects.get(pk = r_id)
    country_stats = models.CountryStats.objects.filter(year = 2018)
    return render(request,'app/list_region.html', {'countries': country_list, 'region': region_list, 'stats': country_stats})

def list_continent(request, c_id):
    country_list = models.Countries.objects.order_by('name')
    region_list = models.Regions.objects.get
    continent_list = models.Continents.objects.get(pk = c_id)
    country_stats = models.CountryStats.objects.filter(year = 2018)
    return render(request,'app/list_continent.html', {'countries': country_list, 'region': region_list, 'continent': continent_list, 'stats': country_stats})

def edit(request, pk):
    country =  models.Countries.objects.get(country_id= pk)
    if request.method == 'POST':
        form = forms.CountryForm1(request.POST, instance= country)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = forms.CountryForm1(instance= country) 
    return render(request, 'app/edit.html', {'form':form})

