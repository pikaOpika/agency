from django.contrib import admin
from django.urls import path

from pages.views import home, documents

app_name = 'pages'

urlpatterns = [
    path('', home, name="home"),
    path('documents/', documents, name="documents"),
]
