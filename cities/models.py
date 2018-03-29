from django.db import models
from django.utils.text import slugify


class CountryCode(models.Model):
    code = models.CharField('Country code', max_length=8)

    def __str__(self):
        return self.code


class City(models.Model):
    country = models.ForeignKey(CountryCode, on_delete='CASCADE')
    city_as = models.CharField('ASCII City Name', max_length=32)
    city_name = models.CharField('City name', max_length=32)
    region = models.CharField('Region', max_length=32)
    population = models.IntegerField('Population')
    latitude = models.FloatField('Latitude', max_length=32)
    longitude = models.FloatField('Longitude', max_length=32)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.city_as, allow_unicode=True)
        super(City, self).save(*args, **kwargs)

    def __str__(self):
        return self.city_as
