"""
URL configuration for ShopifyApi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from store.home import *
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("api/v1/",include([
        path('',include(('store.urls','store'),namespace="Store")),
        path("swagger/schema",schema_view.with_ui("swagger",cache_timeout=0),name="swagger-schema")

    ])),
    path('admin/', admin.site.urls),
]
