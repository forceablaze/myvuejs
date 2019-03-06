from django.conf.urls import url
from .views import LogListAPIView, LogRetrieveAPIView
from .views import LogListCreateAPIView

app_name = 'cvlog'
urlpatterns = [
    url(r'^cvlog/$', LogListCreateAPIView.as_view()),
    url(r'^cvlog/(?P<log_id>\w+)/?$', LogRetrieveAPIView.as_view()),
]
