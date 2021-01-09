from django.shortcuts import render, get_list_or_404
from .models import *
from django.views.generic import ListView, DetailView
# Create your views here.
class Home(ListView):
    model = Restaurant
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class RestaurantDetailView(ListView):
    template_name = 'restaurantDetails.html'

    def get_queryset(self):
        self.orderlist = get_list_or_404(OrderList, restaurant__id=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orderlist'] = self.orderlist
        return context
