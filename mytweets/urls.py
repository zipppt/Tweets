from django.conf.urls import patterns, include, url
from django.contrib import admin
from tweets.views import Index, Profile, PostTweet, HashTagCloud

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', Index.as_view()),
    url(r'^user/(\w+)/$', Profile.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/(\w+)/post/$', PostTweet.as_view()),
    url(r'^hashTag/(\w+)/$', HashTagCloud.as_view()),
)
