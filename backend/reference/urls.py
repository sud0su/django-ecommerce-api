from django.urls import path
from .views import *

urlpatterns = [
    path('carrier/list/', CarrierList.as_view(), name="carriers-all"),
    path('carrier/create/', CarrierCreate.as_view()),
    path('carrier/update/<int:pk>/', CarrierRetrieveUpdate.as_view()),
]