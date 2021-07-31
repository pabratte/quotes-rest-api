from django.conf.urls import url
from . import api


urlpatterns = [
    url(r'quotes/(?P<pk>\d+)', api.QuoteApiView.as_view(), name='quotes-retrieve'),
    url(r'quotes/', api.QuoteListApiView.as_view(), name='quotes-list'),
]
