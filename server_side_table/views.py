from django.core.exceptions import ImproperlyConfigured
from django.db.models import Q, QuerySet, Sum
from django.http import JsonResponse
from django.shortcuts import render
from django_serverside_datatable import datatable
from django_serverside_datatable.views import ServerSideDatatableView

from server_side_table.models import ApiDatatable


# Create your views here.
class ApiView(ServerSideDatatableView):
    """
    This is the view function that manage the GET, PUT, POST &
    DELETE e.t.c operations
    """

    queryset = ApiDatatable.objects.all()
    columns = ['organization_name', 'api_name', 'date', 'usages']

    def get(self, request, *args, **kwargs):
        result = datatable.DataTablesServer(
            request, self.columns, self.get_queryset()).output_result()
        sum = self.get_queryset().aggregate(sum=Sum('usages'))
        search = ''
        search = self.request.GET.get('sSearch')
        if search != '':
            sum = self.get_queryset().filter(
                Q(organization_name__contains=search) |
                Q(api_name__contains=search) |
                Q(date__contains=search) |
                Q(usages__contains=search)
            ).aggregate(sum=Sum('usages'))
            result.update(sum)
        else:
            result.update(sum)
        return JsonResponse(result, safe=False)

    def get_queryset(self):
        """
        Return the list of items for this view.
        """

        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        api_name = self.request.GET.get('api_name')
        if start_date and end_date and api_name is not None:
            queryset = ApiDatatable.objects.filter(date__range=(start_date, end_date), api_name=api_name)
        elif start_date and end_date is not None and api_name is None:
            queryset = ApiDatatable.objects.filter(date__range=(start_date, end_date))
        elif api_name is not None:
            queryset = ApiDatatable.objects.filter(api_name=api_name)
        elif self.queryset is not None:
            queryset = self.queryset
            if isinstance(queryset, QuerySet):
                queryset = queryset.all()
        elif self.model is not None:
            queryset = self.model._default_manager.all()
        else:
            raise ImproperlyConfigured(
                "%(cls)s is missing a QuerySet. Define "
                "%(cls)s.model, %(cls)s.queryset, or override "
                "%(cls)s.get_queryset()." % {
                    'cls': self.__class__.__name__
                }
            )

        return queryset


def home(request):
    api_list = ApiDatatable.objects.values('api_name')
    context = {"api":api_list}

    return render(request, "home.html", context)
