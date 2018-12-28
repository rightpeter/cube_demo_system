from django.conf.urls import url
from users import views


urlpatterns = [
    url('', views.HomePageView.as_view()),
]
