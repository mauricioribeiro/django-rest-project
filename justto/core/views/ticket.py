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
    pass


class TicketRetrieveUpdateDestroyView(TicketView, RetrieveUpdateDestroyAPIView):
    pass


class TicketListCreateViewAsMemCached(TicketView, ListCreateAPIView):

    @method_decorator(cache_page(60, cache='default'))
    def dispatch(self, request, *args, **kwargs):
        return super(TicketListCreateViewAsMemCached, self).dispatch(request, *args, **kwargs)


class TicketRetrieveUpdateDestroyViewAsMemCached(TicketView, RetrieveUpdateDestroyAPIView):

    @method_decorator(cache_page(60, cache='default'))
    def dispatch(self, request, *args, **kwargs):
        return super(TicketRetrieveUpdateDestroyViewAsMemCached, self).dispatch(request, *args, **kwargs)


class TicketListCreateViewAsRedis(TicketView, ListCreateAPIView):

    @method_decorator(cache_page(60, cache='default'))
    def dispatch(self, request, *args, **kwargs):
        return super(TicketListCreateViewAsRedis, self).dispatch(request, *args, **kwargs)


class TicketRetrieveUpdateDestroyViewAsRedis(TicketView, RetrieveUpdateDestroyAPIView):

    @method_decorator(cache_page(60, cache='default'))
    def dispatch(self, request, *args, **kwargs):
        return super(TicketRetrieveUpdateDestroyViewAsRedis, self).dispatch(request, *args, **kwargs)