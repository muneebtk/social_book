from django.contrib import admin
from .models import Account, Books
# Register your models here.


@admin.register(Account)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ['password']


@admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    pass
