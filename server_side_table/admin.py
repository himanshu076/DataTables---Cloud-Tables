from django.contrib import admin
from server_side_table.models import ApiDatatable

# Register your models here.

class ApiDatatableAdmin(admin.ModelAdmin):
    list_display = ("id", "organization_name", "api_name",
                    "date", "usages")
    list_filter = ("organization_name", "api_name")
    fields = ("organization_name", "api_name", "usages")

    list_per_page = 8
    ordering = ['-date']
    search_fields = ["organization_name", "api_name"]


admin.site.register(ApiDatatable, ApiDatatableAdmin)