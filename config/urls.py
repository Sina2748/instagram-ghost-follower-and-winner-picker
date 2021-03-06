# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # User management
    path('accounts/', include('django.contrib.auth.urls')),

    # Local apps
    path('accounts/', include('accounts.urls')), # new
    path('', include('pages.urls')),
    # Local apps
    path('books/', include('books.urls')), # new
    path('insta/', include('insta_app.urls')), # new

]

