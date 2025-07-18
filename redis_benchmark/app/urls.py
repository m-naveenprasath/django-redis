from django.urls import path
from . import views

urlpatterns = [
    path('no-cache/', views.no_cache_view),
    path('with-cache/', views.with_cache_view),
]
