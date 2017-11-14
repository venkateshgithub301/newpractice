from django.contrib import admin

# Register your models here.
from .models import book,MultiBooks,MultiAuthorsandBooks
admin.site.register(book)
admin.site.register(MultiBooks)
admin.site.register(MultiAuthorsandBooks)