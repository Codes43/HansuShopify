from django.urls import path
from .views import SignInView,SignUpView,ListProductsView,CreateProductView

urlpatterns=[
    path("signin/",SignInView.as_view(),name='signin'),
    path("signup/",SignUpView.as_view(),name='signup'),
    ##urls for the products
    path("products",ListProductsView.as_view(),name="products"),
    path("products/create",CreateProductView.as_view(),name="create-product")
]