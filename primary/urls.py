from django.urls import path

from primary.views import index, special

urlpatterns = [
    path('special', special, name='special'),
    path('', index, name='home'),

]
