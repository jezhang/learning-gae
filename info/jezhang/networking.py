# -*- coding: utf-8 -*-

import urllib2  

'''
Python urllib2 通过content-length头获取文件大小
通过HEAD方法可以只读取HTTP应答头而不用下载文件本身，这样可以节省时间和资源。
常规的方式是使用httplib，这里选择使用urllib2主要是考虑要支持代理。
'''  
def get_file_size_by_url(url, proxy=None):  
    opener = urllib2.build_opener()  
    if proxy:  
        if url.lower().startswith('https://'):  
            opener.add_handler(urllib2.ProxyHandler({'https' : proxy}))  
        else:  
            opener.add_handler(urllib2.ProxyHandler({'http' : proxy}))  
    request = urllib2.Request(url)  
    request.get_method = lambda: 'HEAD'  
    try:  
        response = opener.open(request)  
        response.read()  
    except Exception, e:  
        print '%s %s' % (url, e)  
    else:  
        return dict(response.headers).get('content-length', 0) 

