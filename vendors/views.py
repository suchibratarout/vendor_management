from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Vendor
from .serializers import VendorSerializer
from django.http import Http404
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer
from rest_framework import generics
from django.shortcuts import render
from django.utils import timezone
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.generic import View






class VendorListCreateAPIView(APIView):
    def get(self, request):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VendorRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, vendor_id):
        try:
            return Vendor.objects.get(pk=vendor_id)
        except Vendor.DoesNotExist:
            raise Http404

    def get(self, request, vendor_id):
        vendor = self.get_object(vendor_id)
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)

    def put(self, request, vendor_id):
        vendor = self.get_object(vendor_id)
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, vendor_id):
        vendor = self.get_object(vendor_id)
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PurchaseOrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


def order_dashboard(request):
    orders = PurchaseOrder.objects.all()
    return render(request, 'index.html', {'orders': orders})



class VendorPerformanceAPIView(APIView):
    def get(self, request, vendor_id):
        try:
            vendor = Vendor.objects.get(id=vendor_id)
            performance_metrics = {
                "on_time_delivery_rate": vendor.on_time_delivery_rate,
                "quality_rating_avg": vendor.quality_rating_avg,
                "average_response_time": vendor.average_response_time,
                "fulfillment_rate": vendor.fulfillment_rate
            }
            return Response(performance_metrics)
        except Vendor.DoesNotExist:
            return Response({"error": "Vendor not found"}, status=404)



class PurchaseOrderAcknowledgmentAPIView(APIView):
    def post(self, request, po_id):
        try:
            purchase_order = PurchaseOrder.objects.get(id=po_id)
            purchase_order.acknowledgment_date = timezone.now()
            purchase_order.save()
            # Trigger recalculation of average_response_time here (not implemented in this example)
            return Response({"success": "Acknowledgment updated"})
        except PurchaseOrder.DoesNotExist:
            return Response({"error": "Purchase order not found"}, status=404)


class UserLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserRegistration(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, password=password)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)




class MyView(View):
    def get(self, request):
        # Your logic for handling GET requests
        current_time = timezone.now()
        data = {
            'message': 'Hello from Django!',
            'current_time': current_time.strftime('%Y-%m-%d %H:%M:%S')
        }
        return JsonResponse(data)

    def post(self, request):
        # Your logic for handling POST requests
        data = request.POST.get('data')
        # Process the data as needed
        response_data = {
            'message': 'Received POST request with data: {}'.format(data)
        }
        return JsonResponse(response_data)


def vendors_view(request):
    # Fetch all vendors from the database
    vendors = Vendor.objects.all()

    # Pass the vendors as context data to the template
    context = {
        'vendors': vendors,  # Pass the vendors queryset to the template
    }
    return render(request, 'vendors.html', context)