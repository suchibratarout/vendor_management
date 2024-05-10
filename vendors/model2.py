# from django.db import models
# from .models import PurchaseOrder  # Import the PurchaseOrder model
#
# class OrderStatusHistory(models.Model):
#     order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
#     new_status = models.CharField(max_length=20)
#     timestamp = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"{self.order.po_number} - {self.new_status} ({self.timestamp})"


# models.py

from django.db import models
from .models import PurchaseOrder  # Import the PurchaseOrder model


class OrderStatusHistory(models.Model):
    # Define choices for order status
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),
    ]

    # Define fields for the OrderStatusHistory model
    order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    new_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    # Define a string representation for the model
    def __str__(self):
        return f"Order: {self.order.po_number}, New Status: {self.new_status}, Timestamp: {self.timestamp}"
