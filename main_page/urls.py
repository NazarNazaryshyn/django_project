from django.urls import path, include
from .views import main_page


app_name = 'main_page'


urlpatterns = [
    path('', main_page, name='home')
]
