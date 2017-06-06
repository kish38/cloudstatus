# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#!/usr/bin/env python

from pymongo import MongoClient
from json import dumps
#variables
def get_regions_list():
	mongo_server = "mongodb://13.126.35.194:27017"
	client = MongoClient( mongo_server )
	geo_regions = ['NA', 'SA', 'AP', 'EU' ]

	#connection to database
	db = client['amazon']
	collections = db.collection_names()
	reg = []

	for i in range(len(geo_regions)):
	    collection = db[geo_regions[i]]
	    a = collection.find({}, {"service": 1})

	    for row in a:
	        k = row["service"].split('(')

	        try:
	            v = k[1].split(')')[0].encode('ascii', 'ignore')
	            reg.append(v)


	        except IndexError:
	            no_data = "null"

	dc = list(sorted(set(reg)))
	return {'regions':dc}


def get_regions(request):
	return render(request,'regions.html',{'regions':get_regions_list()})
	return HttpResponse(dumps(get_regions_list()), content_type = "application/json")