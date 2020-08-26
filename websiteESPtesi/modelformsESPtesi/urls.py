from django.conf.urls import url

from modelformsESPtesi import views

app_name = 'modelformsESPtesi'

urlpatterns = [

    # /modelformsESPtesi/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # modelformsESPtesi/product/entry
    url(r'^espdata/entry/$',views.ESPdataEntry.as_view(),name='espdata-entry'),

    # modelformsESPtesi/product/2
    url(r'^espdata/(?P<pk>[0-9]+)/$', views.ESPdataUpdate.as_view(), name='espdata-update'),

    # modelformsESPtesi/product/(?P<pk>[0-9]+)/delete
    url(r'^album/(?P<pk>[0-9]+)/delete$', views.ESPdataDelete.as_view(), name='espdata-delete'),

]