from django.conf.urls import url, include
from . import views
app_name = 'Mcapi'

urlpatterns = [
    url(r'^predict/$', views.func, name = 'dashboard')
]