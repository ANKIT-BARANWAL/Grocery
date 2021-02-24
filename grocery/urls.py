from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from groceries import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('groceries.urls')),
    path('api/',views.GroceryList.as_view()),
]