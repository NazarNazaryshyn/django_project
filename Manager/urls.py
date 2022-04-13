from django.urls import path, include
from .views import reservation_list, update_reservation


app_name = 'Manager'


urlpatterns = [

    path('reservations/', reservation_list, name='reservation_list'),
    path('reservations/update/<int:pk>/', update_reservation, name='update_reservation')

]