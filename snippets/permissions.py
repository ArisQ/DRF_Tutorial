from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    只有Object的拥有者才能修改
    """

    def has_object_permission(self, request, view, obj):
        # 任何人都可以读取，因此Get，Head，Options始终允许
        if request.method in permissions.SAFE_METHODS:
            return True
        # 写入需要所有者权限
        return obj.owner == request.user
