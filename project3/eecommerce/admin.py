from django.contrib import admin
from .models import User,Categories,Product,Order
# Register your models here.

admin.site.register(User)
admin.site.register(Categories)
admin.site.register(Product)
admin.site.register(Order)