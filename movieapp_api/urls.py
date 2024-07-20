from django.contrib import admin
from django.urls import path, include
from movies.views import home  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('movies.urls')),
    path('', home),  
]
