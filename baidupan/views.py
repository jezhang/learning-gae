# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect

def oauth_redirect(request):
	code = request.GET.get('code',None)
	if code is not None:
		return HttpResponse(code)
	else:
		return None