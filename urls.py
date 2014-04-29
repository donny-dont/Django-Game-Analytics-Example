from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url('^upload_log/$', 'game.views.upload_log'),
	url('^quests/', 'analytics.views.quests'),
	url('^quest_statistics/(\d+)/$', 'analytics.views.quest_statistics'),
	url('^players/', 'analytics.views.players'),
	url('player_statistics/start/(\d\d\d\d)/(\d{1,2})/(\d{1,2})/end/(\d\d\d\d)/(\d{1,2})/(\d{1,2})/$', 'analytics.views.player_statistics'),
  url(r'^admin/', include(admin.site.urls)),
)
