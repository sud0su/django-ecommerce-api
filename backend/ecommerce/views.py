from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

# Create your views here.
class Home(TemplateView):
    title = "Dashboard"
    template = "dashboard/index.html"

    def get(self, request, *args, **kwargs):
        context = {"title": self.title, "data": "tess"}
        return render(request, self.template, context)
