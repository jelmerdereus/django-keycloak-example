from django.urls import path

from primary.views import *

urlpatterns = [
    path('', index, name='home'),
]
