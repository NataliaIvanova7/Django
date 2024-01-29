from django.core.management.base import BaseCommand, CommandParser
import datetime

from homework_app.models import Product


class Command(BaseCommand):
    help = 'Creates fake products to fill DB'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('count', type=int, help='Number of products')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for i in range(1, count + 1):
            product = Product(
                title=f'Product{i}',
                description=f'some text',
                price=10.50,
                count=i,
                )
            
            self.stdout.write(f'Product {product} was created')
            product.save()



