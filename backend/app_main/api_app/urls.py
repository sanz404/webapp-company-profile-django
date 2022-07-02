from django.urls import path
from .views import ContactViews

urlpatterns = [
    path('contacts/', ContactViews.as_view())
]