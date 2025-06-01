from django.urls import path
from .views import SignInView,SignUpView,ListProductsView,CreateProductView,ProductDetailView,DeleteProductView,UpdateProductView

urlpatterns=[
    path("signin/",SignInView.as_view(),name='signin'),
    path("signup/",SignUpView.as_view(),name='signup'),
    ##urls for the products
    path("products/",ListProductsView.as_view(),name="products"),
    path("products/create/",CreateProductView.as_view(),name="create-product"),
    path("products/<int:pk>/",ProductDetailView.as_view(),name="product-details"),
    path("products/update/<int:pk>/",UpdateProductView.as_view(),name="update-product"),
    path("products/delete/<int:pk>/",DeleteProductView.as_view(),name="delete-product")


]