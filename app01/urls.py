
from django.conf.urls import url,include

from app01 import views


urlpatterns = [
    url(r'^$',views.index),
    url(r'cash/$',views.pay_by_cash),
    url(r'p1/$',views.pag01),
    url(r'^book/$',views.book),
    url(r'^articles/([0-9]{4})/$', views.year_archive,{'file_type':'json'}),
]
