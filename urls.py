from django.contrib import admin
from django.urls import path
from generator_app.views import generate_excel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate-excel/', generate_excel, name='generate_excel'),
]
