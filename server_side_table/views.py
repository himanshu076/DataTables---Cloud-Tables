import re
from urllib import request
from django.db.models import Q
from django.shortcuts import render
from django.utils.html import escape
from django_datatables_view.base_datatable_view import BaseDatatableView
from django_serverside_datatable.views import ServerSideDatatableView

from server_side_table.models import ApiDatatable


from django.views import View
from django.http import JsonResponse
from django.core.exceptions import ImproperlyConfigured
from django.db.models import QuerySet
from django_serverside_datatable import datatable

# Create your views here.




# class ApiView(BaseDatatableView):
#     # The model we're going to show
#     model = ApiDatatable

#     # define the columns that will be returned
#     columns = ['organization_name', 'api_name', 'date', 'usages']

#     # define column names that will be used in sorting
#     # order is important and should be same as order of columns
#     # displayed by datatables. For non-sortable columns use empty
#     # value like ''
#     order_columns = ['organization_name', 'api_name', 'date', 'usages']

#     # set max limit of records returned, this is used to protect our site if someone tries to attack our site
#     # and make it return huge amount of data
#     max_display_length = 500

#     def render_column(self, row, column):
#         # We want to render user as a custom column
#         if column == 'user':
#             # escape HTML for security reasons
#             return escape('{0} {1}'.format(row.customer_firstname, row.customer_lastname))
#         else:
#             return super(ApiView, self).render_column(row, column)

#     def filter_queryset(self, qs):
#         # use parameters passed in GET request to filter queryset

#         # simple example:
#         search = self.request.GET.get('search[value]', None)
#         if search:
#             qs = qs.filter(name__istartswith=search)

#         # more advanced example using extra parameters
#         filter_customer = self.request.GET.get('customer', None)

#         if filter_customer:
#             customer_parts = filter_customer.split(' ')
#             qs_params = None
#             for part in customer_parts:
#                 q = Q(customer_firstname__istartswith=part) | Q(customer_lastname__istartswith=part)
#                 qs_params = qs_params | q if qs_params else q
#             qs = qs.filter(qs_params)
#         return qs


# self.request.get

class ApiView(ServerSideDatatableView):

    queryset = ApiDatatable.objects.all()
    columns = ['organization_name', 'api_name', 'date', 'usages']

    def get_queryset(self):
        # breakpoint()
        """
        Return the list of items for this view.

        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        if self.queryset is not None:
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

    def post(self, request, *args, **kwargs):
        breakpoint()
        if self.queryset is not None:
            queryset = self.queryset
            if isinstance(queryset, QuerySet):
                queryset = queryset.all()
        elif self.model is not None:
            queryset = self.model._default_manager.all()

        return self.get(request, *args, **kwargs)

def home(request):
    # breakpoint
    # all_api = ApiDatatable.objects.all()
    # context = {"api":all_api}
    return render(request, "home.html")
