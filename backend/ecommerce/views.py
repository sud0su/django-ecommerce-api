from django.shortcuts import render, get_object_or_404
from django.http import Http404
# from .models import Question
# Create your views here.
def Home(request):
    # data = Question.objects.all()
    template = "dashboard/index.html"
    title = "Dashboard Info"
    context = {"title": title, "data": "tess"}
    return render(request, template, context)
