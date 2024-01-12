
from django.contrib import admin
from django.urls import path, include
from homepageapi.views import query_list
from rest_framework import routers
from resultpageapi.views import list_view

# router = routers.SimpleRouter()
# router.register('', query_list)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/query/', query_list, name='query_list'),
    path('api/results/', list_view, name='list-view'),
]
