import csv
import pandas as pd
from django.core.management.base import BaseCommand
from orders.models import Product

class Command(BaseCommand):
    help = 'Update inventory from XLSX or CSV file'

    def handle(self, *args, **kwargs):
        xlsx_file = r'C:\Users\carol\Downloads\update_inventory.xlsx'
        csv_file = r'C:\Users\carol\Downloads\update_inventory.csv'

        # Convertir XLSX a CSV
        try:
            df = pd.read_excel(xlsx_file)
            df.to_csv(csv_file, index=False)
            self.stdout.write(self.style.SUCCESS('Successfully converted XLSX to CSV'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error converting XLSX to CSV: {e}'))
            return

        # Leer el archivo CSV y actualizar el inventario
        try:
            with open(csv_file, mode='r') as file:
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
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error reading CSV file: {e}'))
