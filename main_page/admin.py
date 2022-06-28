from django.contrib import admin
from .models import Doctors, Services, UserReservation, Departaments

admin.site.register(Doctors)
admin.site.register(Services)
admin.site.register(UserReservation)
admin.site.register(Departaments)
