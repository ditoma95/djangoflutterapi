from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    produits = Product.objects.all()
    champsrecherche = request.GET.get('itemrechercher')
    if  champsrecherche != '' and champsrecherche is not None:
        produits = Product.objects.filter(title__icontains=champsrecherche)

        # pagination

        #faisons donc la pagination
    paginator = Paginator(produits, 8)
    page = request.GET.get('page')
    produits = paginator.get_page(page)
    return render(request, 'shop/index.html', {'produits': produits})  

def show(request, id):
    unproduit = Product.objects.get(id=id)
    return render(request,'shop/show.html',{'unproduit' : unproduit})

