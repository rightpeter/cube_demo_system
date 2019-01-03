from django.conf.urls import url
from cube import views


urlpatterns = [
    url('upload', views.UploadView.as_view()),
]
