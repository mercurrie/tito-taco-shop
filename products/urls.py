from products import views
from django.urls import path


urlpatterns = [
    path('<int:product_id>/', views.product, name='product-page'),
    path('<int:product_id>/product_images/<str:filename>', views.get_image, name='product-img'),
    path('checkout/<int:product_id>/', views.checkout, name='checkout-page'),
    path('checkout-button/<int:product_id>/', views.checkout_button, name='checkout-button'),
]