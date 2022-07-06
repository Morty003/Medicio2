from django.shortcuts import render, redirect
from .models import Doctors, Services, Departaments, About_Us, Awards, Pricing, Questions
from .forms import UserReservationForm


def main_page(request):
    if request.method == 'POST':
        reservation = UserReservationForm(request.POST)
        if reservation.is_valid():
            reservation.save()
            return redirect('/')

    reservation = UserReservationForm()
    doctors = Doctors.objects.filter(is_visible=True).order_by('position')
    services = Services.objects.filter(is_visible=True).order_by('position')
    departments = Departaments.objects.filter(is_visible=True).order_by('position')
    about_us = About_Us.objects.all
    awards = Awards.objects.all
    pricing = Pricing.objects.filter(is_visible=True)
    questions = Questions.objects.filter(is_visible=True)

    return render(request, 'main.html', context={
        'doctors': doctors,
        'services': services,
        'reservation': reservation,
        'departments': departments,
        'about_us': about_us,
        'awards': awards,
        'pricing': pricing,
        'questions': questions,

        })

