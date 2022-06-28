from django.shortcuts import render, redirect
from .models import Doctors, Services, Departaments
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

    return render(request, 'main.html', context={
        'doctors': doctors,
        'services': services,
        'reservation': reservation,
        'departments': departments,
        })
