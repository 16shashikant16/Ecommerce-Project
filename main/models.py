from django.db import models
from django.contrib.auth.models import User  # Ensure you import the User model

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    



# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
#     product = models.CharField(max_length=255)
#     quantity = models.IntegerField(default=1)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Order {self.id} by {self.user.username}"


from django.db import models

class Order(models.Model):

    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    #user_id = models.ForeignKey(User, on_delete=models.CASCADE)  # Add this field


