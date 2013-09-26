# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

def hello(request):
	return HttpResponse('Hello World!')


def list_nj_ct_shops(request):
	url = 'http://js.189.cn/entityHall_getEntityList.action?areaId=3&cityId=9&busiType=0'
	html = urllib2.urlopen(url).read()
	r = re.compile(r'"cityName":"(.+?)".+?:"(.+?)".+?areaName":"(.+?)".+?:"(.+?)".+?:"(.+?)".+?name":"(.+?)"',re.DOTALL)
    print len(r.findall(html))
    for x in r.findall(html):
        print "%s\t%s\t%s\t%s\t%s\t%s" % (x[0],x[1],x[2],x[3],x[4],x[5])

    return HttpResponse("completed.")



