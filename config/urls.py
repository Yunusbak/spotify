import os
from django.contrib import admin
from django.urls import path, include
from dotenv import load_dotenv
load_dotenv()



ADMIN_URL = os.getenv("ADMIN_URL")

urlpatterns = [
    path(f'{ADMIN_URL}/', admin.site.urls),
    path('', include('api.urls')),
]
