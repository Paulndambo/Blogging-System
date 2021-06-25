from django.shortcuts import render
from . models import Shipment
# Create your views here.
def home(request):
	return render(request, "shipment/index.html")

def search(request):
    return render(request, "shipment/home.html")

def tracking(request):
    if request.method == 'POST':
        searched = request.POST['searched']

        shipments = Shipment.objects.filter(tracking_number__contains=searched)

        return render(request, "shipment/search.html", {'searched': searched, 'shipments': shipments})
    else: 
        return render(request, "shipment/search.html")

def contact(request):
    return render(request, "shipment/contact.html")

def about(request):
    return render(request, "shipment/about.html")

def services(request):
    return render(request, "shipment/services.html")