from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token

from .views.ticket import *
from .views.user import *

urlpatterns = [
    url(r'auth/$', obtain_auth_token, name='core-auth'),

    url(r'^tickets[\/]?$', TicketListCreateView.as_view(), name='ticket-list-create'),
    url(r'^tickets/(?P<pk>[0-9]+)[\/]?$', TicketRetrieveUpdateDestroyView.as_view(), name='ticket-retrieve-update-destroy'),

    url(r'^users[\/]?$', UserListCreateView.as_view(), name='user-list-create'),
    url(r'^users/(?P<pk>[0-9]+)[\/]?$', UserRetrieveUpdateDestroyView.as_view(),
        name='user-retrieve-update-destroy'),
]
