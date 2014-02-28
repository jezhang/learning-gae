# -*- coding:utf-8 -*-

from google.appengine.ext import db


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

class Encrypt(db.Model):
	client_ip = db.StringProperty()    
	request_date = db.DateTimeProperty()
	text = db.StringProperty()

class Website(db.Model):
	company = db.StringProperty()
	url = db.LinkProperty()
	name = db.StringProperty()

	@staticmethod
	def init():
		if Website.all().count() > 0:
			print "already have records in Website"
		else:
			for k,v in QJMY_URLS.items():
				website = Website()
				website.company = 'QJMY'
				website.url = v
				website.name = k
				website.put()

	@staticmethod
	def get_websites_by_company(company):
		websites = Website.all()
		websites.filter('company = ',company)
		return websites


class WebsiteResult(db.Model):
	website = db.ReferenceProperty(Website, required=True)
	dtime_test = db.DateTimeProperty(auto_now_add=True)
	connectability = db.BooleanProperty()
	status_code = db.IntegerProperty()
	message = db.StringProperty()

