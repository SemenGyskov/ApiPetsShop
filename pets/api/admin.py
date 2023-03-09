from django.contrib import admin
from .models import Pet, Type, Stat, Category, Order

admin.site.register(Pet)
admin.site.register(Type)
admin.site.register(Stat)
admin.site.register(Category)
admin.site.register(Order)
