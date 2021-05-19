from . import views
from django.urls import path

app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name = 'home'),
    path('doors', views.doors_page_view, name = 'doors'),
    path('dire', views.dire_page_view, name = 'dire'),
]

