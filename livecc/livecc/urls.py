from django.contrib import admin
from django.urls import path
from liveccapp.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
]


handler404 = "liveccapp.views.pnf" 