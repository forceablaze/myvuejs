from django.conf.urls import url
from .views import FileView

app_name = 'file'
urlpatterns = [
    url(r'^file/$', FileView.as_view()),
]
