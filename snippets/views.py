from rest_framework import generics
from rest_framework import permissions
from snippets.models import Snippet
from snippets.serializers import SnippetModelSerializer
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
from snippets.permissions import IsOwnerOrReadOnly

class SnippetList(generics.ListCreateAPIView):
    """
    列出所有snippet或者创建snippet
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetModelSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    获取，更新，删除snippet
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetModelSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
