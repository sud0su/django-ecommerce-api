from django.contrib import admin
from .models import Order, OrderStatus, OrderProduct, OrderHistory

admin.site.register([Order, OrderProduct, OrderStatus, OrderHistory])
