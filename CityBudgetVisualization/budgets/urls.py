from django.conf.urls import url

from budgets import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]