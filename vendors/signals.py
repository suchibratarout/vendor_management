from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseOrder
from .model2 import  OrderStatusHistory
from django.core.mail import send_mail

@receiver(post_save, sender=PurchaseOrder)
def order_status_change(sender, instance, created, **kwargs):
    if not created:
        # Check if status has changed
        if instance.status != instance.previous_status:
            # Log status change
            OrderStatusHistory.objects.create(order=instance, new_status=instance.status)
            # Send notification (e.g., email)
            send_mail(
                'Order Status Update',
                f'Your order {instance.po_number} has been updated to {instance.status}.',
                'from@example.com',
                [instance.customer.email],
                fail_silently=False,
            )
