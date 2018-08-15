from django.conf.urls import url
from django.urls import path
from snippets import views

urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view(), name='snippet-list'),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet-detail),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^$', views.api_root),
]
