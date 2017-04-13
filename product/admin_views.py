from django.contrib.admin.views.main import ChangeList


class InactiveProductsView(ChangeList):
    def __init__(self, *args, **kwargs):
        super(InactiveProductsView, self).__init__(*args, **kwargs)
        self.list_display = ('name', 'price')

    def get_queryset(self, request):
        qs = super(InactiveProductsView, self).get_queryset(request)
        # filter inactive and admin users
        return qs.filter(active=False)
