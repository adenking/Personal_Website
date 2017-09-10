from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    # ex: /blog/
    url(r'^', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
]
