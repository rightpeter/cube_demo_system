from django.conf.urls import url
from visualization import views


urlpatterns = [
    url('map', views.MapView.as_view()),
]
