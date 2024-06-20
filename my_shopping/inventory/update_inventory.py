import csv
from django.core.management.base import BaseCommand
from orders.models import Product

class Command(BaseCommand):
    help = 'Update inventory from CSV file'

    def handle(self, *args, **kwargs):
        with open('path/to/your/csvfile.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                product_id = row['product_id']
                quantity = int(row['quantity'])
                
                try:
                    product = Product.objects.get(id=product_id)
                    product.stock -= quantity
                    product.save()
                    self.stdout.write(self.style.SUCCESS(f'Successfully updated stock for product {product_id}'))
                except Product.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'Product {product_id} does not exist'))
