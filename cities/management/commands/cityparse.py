from django.core.management.base import BaseCommand
from cities.models import City, CountryCode


class Command(BaseCommand):
    help = 'Parsing cities from txt file to DB'

    def add_arguments(self, parser):
        parser.add_argument('FILE.txt')

    def handle(self, *args, **options):
        with open(options['FILE.txt'], 'r', encoding='ISO-8859-1') as file_in:
            for line in file_in:
                city = line.split(',')

                if line.split(',')[0] != 'Country':
                    country_code = CountryCode.objects.get_or_create(code=city[0])
                    country_code = country_code[0]
                    City.objects.create(
                        country_id=country_code.id,
                        city_as=city[1],
                        city_name=city[2],
                        region=city[3],
                        population=(int(city[4]) if city[4] else 0),
                        latitude=float(city[5]),
                        longitude=float(city[6])
                    )

            print('Successfully!')
