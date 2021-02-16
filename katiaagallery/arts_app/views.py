from django.shortcuts import render
from django.http import HttpResponse
from arts_app.models import Art, About, Category
from arts_app.forms import ContactForm


# Create your views here.
def index(request):

    # Get list of all arts in the gallery
    arts = Art.objects.order_by('title')
    arts_dict = {'arts': arts}
    return render(request, 'arts_app/index.html', context=arts_dict)
    #return HttpResponse(name)

def art_page(request, art_id):

    # get recent arts block
    recent_arts = Art.objects.order_by('?')[:3]
    categories  = Category.objects.order_by('name')
    
    # Get the clicked art information
    try:
        art = Art.objects.get(pk=art_id)
    except Art.DoesNotExist:
        raise Http404("This page does not exist")
    return render(request, 'arts_app/art.html', {'art': art, 'recent_arts': recent_arts, 'categories': categories})

def about_page(request):

    # get about page
    try:
        about = About.objects.get(pk=1)
    except About.DoesNotExist:
        raise Http404("This page doesn't exist")
    return render(request, 'arts_app/about.html',{'about': about})

def category_page(request, cat_id):
    # get recent arts block
    categories  = Category.objects.order_by('name')
    # get recent arts block
    recent_arts = Art.objects.order_by('?')[:3]
    # Get the clicked art information
    try:
        filtered_arts = Art.objects.filter(category = cat_id)
    except Art.DoesNotExist:
        raise Http404("This page does not exist")
    return render(request, 'arts_app/category.html', { 'recent_arts': recent_arts,'filtered_arts': filtered_arts, 'categories': categories})

# add contact
def contact(request):

    
    # get recent arts block
    recent_arts = Art.objects.order_by('?')[:3]
    categories  = Category.objects.order_by('name')
    
    form_class = ContactForm

    return render(request, 'arts_app/contact.html', {'form': form_class, 'recent_arts': recent_arts, 'categories': categories})
