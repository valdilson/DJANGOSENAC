from django.contrib import admin
from django.urls import path, URLResolver, include



urlpatterns : list[URLResolver] =[
    path('admin/', admin.site.urls),
    path('paginas', include('paginas.urls')),
    path('projetos', include('projetos.urls')),
]
