from django import forms
from .models import Product
from .models import Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']




# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = '__all__'  # Includes all fields in the model

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['quantity']  # Ensure this matches the fields in the Order model

# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ['quantity']




