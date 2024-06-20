from django.core.management.base import BaseCommand
from orders.models import Product

class Command(BaseCommand):
    help = 'Create sample products with Pokémon names'

    def handle(self, *args, **kwargs):
        products = [
            {'name': 'bulbasaur', 'stock': 100},
            {'name': 'charmander', 'stock': 150},
            {'name': 'squirtle', 'stock': 200},
        ]
        for product_data in products:
            Product.objects.update_or_create(name=product_data['name'], defaults=product_data)
        self.stdout.write(self.style.SUCCESS('Successfully created products'))
