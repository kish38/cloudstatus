from django.conf.urls import url
from status.views import *

urlpatterns =[
	url(r'^get-regions/$',get_regions),
]
