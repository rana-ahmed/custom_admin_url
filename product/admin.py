from django.contrib import admin
from django.conf.urls import url
from functools import update_wrapper
from .admin_views import InactiveProductsView
from .models import Product


class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'price', 'active')

    def get_urls(self):
        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)
            return update_wrapper(wrapper, view)
        urls = super(ProductAdmin, self).get_urls()
        my_urls = [
            url(r'^inactive/$', wrap(self.changelist_view), name="inactive_products")
        ]
        return my_urls + urls

    def get_changelist(self, request):
        if request.resolver_match.url_name == "inactive_products":
            return InactiveProductsView
        return super(ProductAdmin, self).get_changelist(request)

admin.site.register(Product, ProductAdmin)
