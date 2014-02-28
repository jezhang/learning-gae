# -*- coding: utf-8 -*-

import requests
from requests.exceptions import *
import logging
from django.http import HttpResponse

QJMY_URLS = {
	u'亲近母语论坛':'http://gy.qjmy.cn/bbs/forum.php',
	u'亲近母语主站1':'http://qjmy.cn/',
	u'亲近母语主站2':'http://www.qjmy.cn/',
	u'亲近母语南京学堂':'http://nj.qjmy.cn/',
	u'亲近母语云课堂':'http://edu.qjmy.cn/',
	u'点灯人评选':'http://ddr.qjmy.cn/',
	u'论坛报名':'http://baoming.qjmy.cn/home/',
	u'亲近母语老网站':'http://gy.qjmy.cn/',
	u'点灯人评选工具':'http://pingxuan.qjmy.cn/',
	u'点灯人评选工具后台管理':'http://pingxuan.qjmy.cn/qjmyadmin/',
	u'点灯人评选工具2':'http://ddr.qjmy.cn:81/'
}




def qjmytest(request):
	# vs = '<br/>'.join(QJMY_URLS)
	result = dict()
	vs = ''
	for k,v in QJMY_URLS.items():
		try:
			r = requests.get(v)
		except ConnectionError as e:
			logging.error(e)
			result['%s(%s)' %(k,v)] = e
		except RequestException as e:
			logging.error(e)
			result['%s(%s)' %(k,v)] = e
		except HTTPError as e:
			logging.error(e)
			result['%s(%s)' %(k,v)] = e
		else:
			logging.info('%s(%s)' %(k,v) + str(r.status_code))
			if 200 != r.status_code :
				result['%s(%s)' %(k,v)] = r.status_code
				vs += u'<br/>访问异常(%d) : %s' %(r.status_code,'%s(%s)' %(k,v))
			else:
				vs += u'<br/>访问正常(%d) : %s' %(r.status_code,'%s(%s)' %(k,v))
	vs += "<hr>"
	for k,v in result.items():
		vs += "%s:%s<br/>" %(k,str(v))

	return HttpResponse(vs)


