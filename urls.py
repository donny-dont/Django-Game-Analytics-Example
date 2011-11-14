from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Example:
	# (r'^gameanalytics/', include('gameanalytics.foo.urls')),
	('^upload_log/$', 'game.views.upload_log'),
	('^quests/', 'analytics.views.quests'),
	('^quest_statistics/', 'analytics.views.quest_statistics'),
	('^players/', 'analytics.views.players'),
	('player_statistics/start/(\d\d\d\d)/(\d{1,2})/(\d{1,2})/end/(\d\d\d\d)/(\d{1,2})/(\d{1,2})/$', 'analytics.views.player_statistics'),
	
	# Uncomment the admin/doc line below to enable admin documentation:
	# (r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:],
		'django.views.static.serve',
		{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
	)
