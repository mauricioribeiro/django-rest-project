from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from ..models.ticket import *
from ..serializers.ticket import *


class TicketView:
    def __init__(self):
        self.queryset = Ticket.objects.all()
        self.serializer_class = TicketSerializer


class TicketListCreateView(TicketView, ListCreateAPIView):

    @method_decorator(cache_page(60))
    def dispatch(self, request, *args, **kwargs):
        return super(TicketListCreateView, self).dispatch(request, *args, **kwargs)


class TicketRetrieveUpdateDestroyView(TicketView, RetrieveUpdateDestroyAPIView):

    @method_decorator(cache_page(60))
    def dispatch(self, request, *args, **kwargs):
        return super(TicketRetrieveUpdateDestroyView, self).dispatch(request, *args, **kwargs)
