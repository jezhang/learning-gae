# -*- coding:utf-8 -*-
    
from google.appengine.api import urlfetch
import Cookie
import urllib
import logging


def urldecode(value):
    return  urllib.unquote(urllib.unquote(value)).decode('utf8')
    #return  urllib.unquote(value).decode('utf8')

def urlencode(value):
    return urllib.quote(value.encode('utf8'))

def filterComma(vs):
    if vs.endswith(','):
        newstr = vs[:len(vs)-1]    
        return newstr
    else:
        return vs

def fetch_url(url,data=None):
    opener = URLOpener()
    try:
        response = opener.open(url,data)
        if not 200 == response.status_code :
            logging.error('Can not open URL:%s, return code=%s' %(url,response.status_code))
            return -1
        else:
            logging.info('fetch URL [%s]. return code=%s' %(url, response.status_code))
            return response
    except urlfetch.DownloadError, e:
        # logging.error('Can not open URL:%s, return code=%s\n%s' %(url,response.status_code, e))
        raise e
        return -1

class URLOpener():
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
        return ("".join(a))