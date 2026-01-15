from _settings import urls
from django.urls import path
from app_solar_api.views import Number

urlpatterns = [
    path('', Number.as_view())
]