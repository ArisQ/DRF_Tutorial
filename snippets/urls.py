from django.conf.urls import url
from django.urls import path
from snippets import views

urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view()),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]