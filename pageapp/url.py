from django.contrib import admin
from django.urls import URLPattern, path,include

urlpatterns=[
    path('admin/',admin.site.urls),
    path('',include('pages.urls')),
]