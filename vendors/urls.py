from django.urls import path
from .views import VendorListCreateAPIView, VendorRetrieveUpdateDestroyAPIView
from .views import PurchaseOrderListCreateAPIView, PurchaseOrderRetrieveUpdateDestroyAPIView
from .views import order_dashboard
from .views import VendorPerformanceAPIView,PurchaseOrderAcknowledgmentAPIView
from .views import vendors_view

urlpatterns = [
    path('api/vendors/', VendorListCreateAPIView.as_view(), name='vendor-list-create'),
    path('api/vendors/<int:vendor_id>/', VendorRetrieveUpdateDestroyAPIView.as_view(), name='vendor-retrieve-update-destroy'),

    path('api/purchase_orders/', PurchaseOrderListCreateAPIView.as_view(), name='purchase-order-list-create'),
    path('api/purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDestroyAPIView.as_view(), name='purchase-order-retrieve-update-destroy'),
    path('dashboard/', order_dashboard, name='order_dashboard'),
    path('api/vendors/<int:vendor_id>/performance/', VendorPerformanceAPIView.as_view(), name='vendor-performance'),
    path('api/purchase_orders/<int:po_id>/acknowledge/', PurchaseOrderAcknowledgmentAPIView.as_view(), name='purchase-order-acknowledge'),
    path('', vendors_view, name='vendors'),

]


