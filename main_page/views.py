from django.views.generic import ListView
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, Http404
from .models import Category, Dish, Advantage, Chef, Gallery, Slide, Customer, Photo
from .forms import UserReservationForm, UserContactsForm
from django.core.paginator import Paginator
from django.db.models import Avg, Count, Sum

dishes = Dish.objects.filter(is_visible=True).order_by('position')

def main_page(request):
    if request.method == 'POST':
        reservation = UserReservationForm(request.POST)
        contacts = UserContactsForm(request.POST)
        if reservation.is_valid():
            reservation.save()
            return redirect('/')
        if contacts.is_valid():
            contacts.save()
            return redirect('/')

    contacts = UserContactsForm()
    reservation = UserReservationForm()
    c = Category.objects.filter(is_visible=True).order_by('position')
    dishes = Dish.objects.filter(is_visible = True).select_related('category').order_by('position')
    special_dishes = Dish.objects.filter(is_special=True).order_by('position')
    advantages = Advantage.objects.filter(id__lte=3)
    chefs = Chef.objects.all().order_by('id')
    gall = Gallery.objects.filter(is_visible=True)
    slide = Slide.objects.filter(is_visible=True)
    photo_about = Photo.objects.filter(name='photo_about')


    return render(request, 'main.html', context={'c':c,
                                                 'dishes':dishes,
                                                 'special_dishes':special_dishes,
                                                 'advantages':advantages,
                                                 'chefs': chefs,
                                                 'gall':gall,
                                                 'slide':slide,
                                                 'photo_about':photo_about,
                                                 'reservation':reservation,
                                                 'contacts':contacts,
                                                 })



def pagination(request):

    dish = Dish.objects.all()
    paginator = Paginator(dish, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'test_chef.html', {'dish':dish,
                                              'page_obj':page_obj})

