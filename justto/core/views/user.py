from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from ..models.user import *
from ..serializers.user import *


class UserView:
    def __init__(self):
        self.queryset = User.objects.all()
        self.serializer_class = UserSerializer


class UserListCreateView(UserView, ListCreateAPIView):
    pass


class UserRetrieveUpdateDestroyView(UserView, RetrieveUpdateDestroyAPIView):
    pass


class UserListCreateViewAsMemcached(UserView, ListCreateAPIView):

    @method_decorator(cache_page(60))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListCreateViewAsMemcached, self).dispatch(request, *args, **kwargs)


class UserRetrieveUpdateDestroyViewAsMemcached(UserView, RetrieveUpdateDestroyAPIView):

    @method_decorator(cache_page(60))
    def dispatch(self, request, *args, **kwargs):
        return super(UserRetrieveUpdateDestroyViewAsMemcached, self).dispatch(request, *args, **kwargs)