from django.views.generic import DetailView, ListView
from .models import City


class CityListView(ListView):
    model = City
    template_name = 'list_cities.html'
    context_object_name = 'list'
    paginate_by = 100
    queryset = City.objects.all()


class CityDetailView(DetailView):
    model = City
    template_name = 'detail_cities.html'
    context_object_name = 'detail'
