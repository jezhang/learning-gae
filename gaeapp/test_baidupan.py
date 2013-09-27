
from google.appengine.api import urlfetch
import urllib2
from pcs import Client

ACCESS_TOKEN = '3.d1835ee236e603961f013e2099fc2193.2592000.1382851881.1144098186-1469382'
URI = {'file': 'https://pcs.baidu.com/rest/2.0/pcs/file',
       'quota': 'https://pcs.baidu.com/rest/2.0/pcs/quota',
       'thumbnail': 'https://pcs.baidu.com/rest/2.0/pcs/thumbnail',
       'stream': 'https://pcs.baidu.com/rest/2.0/pcs/stream',
       'cloud_dl': 'https://pcs.baidu.com/rest/2.0/pcs/services/cloud_dl'}


def get_baidupan_quota():
	url = 'https://pcs.baidu.com/rest/2.0/pcs/quota?method=%s&access_token=%s' %('info',ACCESS_TOKEN)
	print url
	html = urllib2.urlopen(url).read()	
	print html

def post_single_file_to_baidupan():
	# txt = open('test.txt').read()
	# print txt
	url = 'https://pcs.baidu.com/rest/2.0/pcs/file?path=%s&method=upload&access_token=%s' %('test.txt',ACCESS_TOKEN)
	print url

def info():
	params = {'method': 'info','access_token': ACCESS_TOKEN}
	result = urlfetch.fetch(url=URI['quota'],
				payload=params,
				method=urlfetch.GET
				)
	print result

def post_to_baidupan():
	# local_file = open('text.txt','rb').read()
	# url = 'https://pcs.baidu.com/rest/2.0/pcs/file?path=%s&method=upload&access_token=%s' %('test.txt',ACCESS_TOKEN)
	# print url
	client = Client('3.d1835ee236e603961f013e2099fc2193.2592000.1382851881.1144098186-1469382')
	print client.info()
	# print client.upload_single('jezhang','test.txt')




def main():
	# get_baidupan_quota()
	# post_single_file_to_baidupan()
	# post_to_baidupan()
	info()



if __name__ == '__main__':
	main()