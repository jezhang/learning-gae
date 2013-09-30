# -*- coding:utf-8 -*-

'''
Created on 2012-9-17

@author: jezhang
'''

from google.appengine.api import urlfetch,memcache, users
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
import Cookie
import datetime
import logging
import urllib

logging.info('module base reloaded')

def go_page(request):
    return HttpResponseRedirect('http://www.baidu.com/')    

def login_required(func):
    def _wrapper(request, *args, **kw):
        user = users.get_current_user()
        if user and (user.email() == "babyanuo@gmail.com" or user.email() == "jean.zhang.cn@gmail.com" or user.email() == "yz.zhang.dong@gmail.com"):
            return func(request, *args, **kw)
        else:
            return HttpResponseRedirect(users.create_login_url(request.get_full_path()))
    return _wrapper 


def filterComma(vs):
    if vs.endswith(','):
        newstr = vs[:len(vs)-1]    
        return newstr
    else:
        return vs
      
def gbk2utf8(vs):
    return vs.decode('gbk').encode('utf-8')    

def to_utf8(vs):
    return vs.encode('utf-8')

def get_bj_time():    
    return datetime.datetime.utcnow() + datetime.timedelta(hours=+8)

def urldecode(value):
    return  urllib.unquote(urllib.unquote(value)).decode('utf8')
    #return  urllib.unquote(value).decode('utf8')

def urlencode(value):
    return urllib.quote(value.encode('utf8'))

def sid():
    now=get_bj_time()
    return now.strftime('%y%m%d%H%M%S')+str(now.microsecond)

def today():
#    now = datetime.datetime.date();
    return get_bj_time().strftime('%Y%m%d')
#    return time.strftime('%Y%m%d',time.localtime(time.time()))


class Browser():
    def __init__(self):
        self.cookie = Cookie.SimpleCookie()
        
    def open(self, url, data=None):
        if data is None:
            method = urlfetch.GET
        else:
            method = urlfetch.POST
            
        while url is not None:
            response = urlfetch.fetch(url=url, 
                                      payload=data, 
                                      method=method, 
                                      headers=self._getHeaders(self.cookie),
                                      allow_truncated=False,
                                      follow_redirects=False,
                                      deadline=10
                                      )
            data = None # Next request will be a get, so no need to send the data again. 
            method = urlfetch.GET
            self.cookie.load(response.headers.get('set-cookie', '')) # Load the cookies from the response
            url = response.headers.get('location')
        return response
    
    def _getHeaders(self, cookie):
        headers = {
                   'Host' : 'www.google.com',
                   'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2 (.NET CLR 3.5.30729)',
                   'Cookie' : self._makeCookieHeader(cookie)
                   }    
        return headers
    
    def _makeCookieHeader(self, cookie):        
        a=[""]
        for value in cookie.values():
            a.append("%s=%s; " % (value.key, filterComma(value.value)))
#            cookieHeader += "%s=%s; " % (value.key, filterComma(value.value))
        return ("".join(a))
  
