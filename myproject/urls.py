from django.conf.urls import patterns, include, url

from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'', include('wofw.urls')),
    # url(r'^wards/$', include('wofw.urls')),
    # url(r'^aldermen/$', include('wofw.urls')),
    # url(r'^bills/$', include('wofw.urls'))

)
