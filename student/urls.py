
from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home),
    path('about/', about),
    path('service/', service),
    path('signup/', signup),
    path('newregister/', newregister),
]