from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

# Create your views here.

def home(request ):
    animals = Animals.objects.all()
    return render(request, 'home.html', {'animals': animals})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def animal_detail(request, pk):
    animal = Animals.objects.get(pk=pk)
    return render(request, 'animal_detail.html', {'animal': animal})

def animal_list(request):
    category = request.GET.get('category')
    
    # FILTER
    if category and category != 'all':
        animals = Animals.objects.filter(category=category)
    else:
        animals = Animals.objects.all()
    
    # PAGINATION
    paginator = Paginator(animals, 6)
    page_number = request.GET.get('page')
    animals_page = paginator.get_page(page_number)

    # CATEGORY LIST
    categories = Animals.objects.values_list('category', flat=True).distinct()

    context = {
        'animals': animals_page,
        'categories': categories
    }
    return render(request, 'animal_list.html', context)