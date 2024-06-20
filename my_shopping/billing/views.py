from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from orders.models import Order
from .models import Invoice

@api_view(['POST'])
def generate_invoice(request):
    try:
        order_id = request.data.get('order_id')
        order = Order.objects.get(id=order_id)
        total_amount = order.quantity * order.product.price  # Asumiendo que tienes un campo `price` en Product
        invoice = Invoice.objects.create(order=order, total_amount=total_amount)
        return Response({'message': 'Invoice generated successfully', 'invoice_id': invoice.id}, status=status.HTTP_201_CREATED)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
