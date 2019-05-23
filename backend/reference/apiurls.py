from django.urls import path
from .api import *

urlpatterns = [
    path('carrier/list/', CarrierAPIList.as_view(), name="carriers-all"),
    path('carrier/create/', CarrierAPICreate.as_view()),
    path('carrier/update/<int:pk>/', CarrierAPIRetrieveUpdate.as_view()),
]