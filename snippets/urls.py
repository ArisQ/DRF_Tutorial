from django.conf.urls import url
from django.urls import path
from snippets import views

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
    path('snippets/<int:pk>/', views.snippet_detail),
]