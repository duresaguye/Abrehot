from django.urls import path
from .views import *

app_name = 'Enrollment '

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('search', SearchView.as_view(), name='search'),
]
