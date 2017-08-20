from django.conf.urls import url
from .views import StoreListView, DriverListView, CreateRequestListView, StoreRequestAutocomplete
from dal import autocomplete

urlpatterns = [
    url(r'^stores/$', StoreListView.as_view(), name='store_list'),
    url(r'^drivers/$', DriverListView.as_view(), name='driver_list'),
    url(r'^requests/$', CreateRequestListView.as_view(), name='create_request'),
    url(
        r'^storerequest-autocomplete/$',
        StoreRequestAutocomplete.as_view(),
        name='storerequest-autocomplete',
    ),
]
