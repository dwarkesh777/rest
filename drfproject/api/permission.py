from rest_framework.permissions import BasePermission

class isADMinOrReadonly(BasePermission):
    def has_permission(self, request, view):
        
        if request.method in ["GET","HEAD","OPTION"]:
            return True
        return request.user.is_staff
    