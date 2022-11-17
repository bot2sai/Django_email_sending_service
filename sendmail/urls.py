
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

from .views import contact_view, success_view

urlpatterns = [
    url(r'contact/', contact_view, name='contact'),
    url(r'success/', success_view, name='success'),
]
