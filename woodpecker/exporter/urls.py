from django.conf.urls import url
from django.urls import path

from .views import ExpoterTaskCreateView,ExpoterTaskStatusView, ExpoterFileView

app_name = 'exporter'
urlpatterns = [
    #url(r'^exporter/$', ExpoterTaskCreateView.as_view()),
    path('exporter/', ExpoterTaskCreateView.as_view()),
    path('exporter/<uuid:task_id>', ExpoterTaskStatusView.as_view()),
    path('exporter/download', ExpoterFileView.as_view()),
]
