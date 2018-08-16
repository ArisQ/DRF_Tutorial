from rest_framework import generics
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
from snippets.permissions import IsOwnerOrReadOnly


class SnippetViewSet(viewsets.ModelViewSet):
    """
    通过viewset提供list、CRUD，以及额外的highlight

    retrieve:
    查看指定的snippet

    list:
    列表形式返回所有的snippet

    create:
    新建snippet

    update:
    更新指定的snippet

    delete:
    删除指定的snippet

    highlight:
    返回指定的snippet渲染以后的HTML
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    通过viewset提供list和detail功能
    retrieve:
    返回指定的User。

    list:
    返回所有用户的列表。

    create:
    创建用户
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

