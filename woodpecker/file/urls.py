from django.conf.urls import url
from .views import FileView
from .views import FileStatusView

app_name = 'file'
urlpatterns = [
    url(r'^file/$', FileView.as_view()),
    url(r'^file/(?P<id>\w+)/?$', FileStatusView.as_view()),
]
