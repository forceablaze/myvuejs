from django.conf.urls import url
from .views import LogListAPIView, LogRetrieveAPIView

app_name = 'cvlog'
urlpatterns = [
    url(r'^cvlog/$', LogListAPIView.as_view()),
    url(r'^cvlog/(?P<log_id>\w+)/?$', LogRetrieveAPIView.as_view()),
]
