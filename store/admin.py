from django.contrib import admin
from .models import Author, Category, Ebook, Order, Customer

# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Ebook)
admin.site.register(Order)
admin.site.register(Customer)

