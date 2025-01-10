from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Map root URL to home_view
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.create_product, name='create_product'),
    path('products/edit/<int:product_id>/', views.edit_product, name='edit_product'),  # Correct pattern
    path('products/<int:product_id>/order/', views.order_placement, name='order_placement'),
    path('order/success/', views.order_success, name='order_success'),


]


