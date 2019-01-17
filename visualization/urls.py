from django.conf.urls import url
from visualization import views


urlpatterns = [
    url('county', views.CountyView.as_view()),
    url('city', views.CityView.as_view()),
]
