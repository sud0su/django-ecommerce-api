from django.urls import path
from .views import *

app_name = 'references'
urlpatterns = [
    path('carrier/data/', CarrierView.as_view(), name="carrier-list"),
    path('carrier/create/', CarrierCreateView.as_view(), name="carrier-create"),
    # path('carrier/update/<int:id>', CarrierCreateView.as_view(), name="carrier-create"),
    # path('carrier/delete/<int:id>', CarrierCreateView.as_view(), name="carrier-create"),
]