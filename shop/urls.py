from django.urls import path, include
from django.conf import settings
from . import views
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home', views.homepage, name='home'),
    path('adminka', views.admin_panel, name='adminka'),
    path('create_product', views.create_product, name='create_product'),
    path('register', views.reg, name='register'),
    path('buy', views.add_product, name='buy'),
    path('mycart', views.viewcart, name="viewcart"),
    path('pay', views.pay, name="pay")
]


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)