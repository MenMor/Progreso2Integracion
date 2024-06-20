"""
URL configuration for my_shopping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from billing import views as billing_views
from orders import views as order_views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.shortcuts import redirect

schema_view = get_schema_view(
    openapi.Info(
        title="Billing API",
        default_version='v1',
        description="API for generating invoices",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

def redirect_to_products(request):
    return redirect('list_products')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/invoices/', billing_views.generate_invoice, name='generate-invoice'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('create_order/', order_views.create_order, name='create_order'),
    path('list_products/', order_views.list_products, name='list_products'),
    path('generate_invoice/', billing_views.generate_invoice, name='generate_invoice'), 
    path('products/', order_views.list_products, name='list_products'),  
    path('', redirect_to_products), 
]




