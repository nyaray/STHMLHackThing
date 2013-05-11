from django.conf.urls import patterns, url
from likeamain import views

urlpatterns = patterns('',
    url(r'^$'                    , views.index , name='index') ,
    url(r'^show/(?P<fbID>\d+)/$' , views.show  , name='show')  ,
    url(r''                      , views.uh_oh , name='404')   ,
)
