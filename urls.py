from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gaetemplate.views.home', name='home'),
    # url(r'^gaetemplate/', include('gaetemplate.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^index/$', TemplateView.as_view(template_name="index.html")),
    url(r'^hello/$', 'gaeapp.views.hello', name='hello'),
    url(r'^testpcs/$', 'gaeapp.views.get_baidupan_quota', name='get_baidupan_quota'),    
    url(r'^upload_test/$', 'gaeapp.views.upload_test', name='upload_test'),
    url(r'^telecomshops/$', 'gaeapp.views.list_nj_ct_shops', name='telecomshops'),
    url(r'^GetTelecomNum/$', TemplateView.as_view(template_name="getTelecomNum.html")), # getTelecomNum.html
    url(r'^encrypt/$', 'gaeapp.views.encrypt', name='encrypt'),

    # baidupan required
    url(r'^oauth_redirect/$','baidupan.views.oauth_redirect',name='oauth_redirect'),

    # weixin app
    url(r'^weixin/$', 'gaeapp.views.weixin', name='weixin'),
    


    url(r'^bootstrap/$', TemplateView.as_view(template_name="bootstrap/bootstrap.html")),
)
