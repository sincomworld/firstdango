from django.urls import re_path
from . import views

app_name='music'

urlpatterns = [
    #/music/
    re_path(r'^$', views.index, name='index'),

    #/music/id/
    re_path(r'^(?P<album_id>[0-9]+)/$',views.detail,name='detail')
]
