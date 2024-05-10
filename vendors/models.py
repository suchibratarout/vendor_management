from django.db import models
# from vendors.models import Vendor




class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


# class PurchaseOrder(models.Model):
#     po_number = models.CharField(max_length=100, unique=True)
#     vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
#     order_date = models.DateTimeField()
#     delivery_date = models.DateTimeField()
#     items = models.JSONField()
#     quantity = models.IntegerField()
#     status = models.CharField(max_length=100, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('canceled', 'Canceled')])
#     quality_rating = models.FloatField(null=True)
#     issue_date = models.DateTimeField()
#     acknowledgment_date = models.DateTimeField(null=True)
#
#     def __str__(self):
#         return self.po_number

# models.py



class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),
    ]

    po_number = models.CharField(max_length=100, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.po_number


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.vendor} - {self.date}"
