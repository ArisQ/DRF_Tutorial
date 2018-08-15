from rest_framework import generics
from snippets.models import Snippet
from snippets.serializers import SnippetModelSerializer


class SnippetList(generics.ListCreateAPIView):
    """
    列出所有snippet或者创建snippet
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetModelSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    获取，更新，删除snippet
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetModelSerializer
