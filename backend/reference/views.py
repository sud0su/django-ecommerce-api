from django.http import HttpResponseRedirect
# from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, CreateView, ListView
from django.contrib import messages
from django.urls import reverse
from .models import Carrier
from .forms import *

class CarrierView(ListView):
    template_name = "carrier/index.html"
    queryset = Carrier.objects.all()

class CarrierCreateView(CreateView):
    template_name = "carrier/form.html"
    form_class = CarrierForm
    queryset = Carrier.objects.all()

    def get_success_url(self):
        messages.success(self.request, 'Form Added Successfully')
        return reverse('references:carrier-list')

    def form_valid(self, form):
        messages.success(self.request, 'form is valid')
        form.save()
        return HttpResponseRedirect(self.get_success_url())
