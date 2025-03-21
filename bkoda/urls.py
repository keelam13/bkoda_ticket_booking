"""
URL configuration for bkoda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from reservation import views

print("urls called")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.home_page, name='home'),
    path('find_trip', views.find_trip, name="find_trip"),
    path(
        'origin-autocomplete/',
        views.OriginAutocomplete.as_view(),
        name='origin-autocomplete',
    ),
    path(
        'destination-autocomplete/',
        views.DestinationAutocomplete.as_view(),
        name='destination-autocomplete',
    ),
    path('create/<int:trip_id>', views.make_reservation, name="make_reservation"),
    path('reservation_list/', views.reservation_list, name="reservation_list"),
    path('edit/<int:reservation_id>/', views.edit_reservation, name='edit_reservation'),
    path('cancel/<int:reservation_id>/', views.cancel_reservation, name='cancel_reservation'),
]
