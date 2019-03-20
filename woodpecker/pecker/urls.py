from django.conf.urls import url
from django.urls import path

from .views import PeckerTaskStatusView, PeckerTaskCreateView
from .views import CVLogRetrieveView

app_name = 'pecker'
urlpatterns = [
    url(r'^pecker/$', PeckerTaskCreateView.as_view()),
    path('pecker/cvlog/<uuid:task_id>', CVLogRetrieveView.as_view()),
    path('pecker/<uuid:task_id>', PeckerTaskStatusView.as_view()),
]
