from django.contrib import admin
from .models import Query
# Register your models here.

@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    list_display = ['id', 'query', 'k_value']