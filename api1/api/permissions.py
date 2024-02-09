from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in permissions.SAFE_METHODS:
                return True
            # Allow authenticated staff users to create tasks
            return request.user.role.type == 'staff'

        #if request.user.is_authenticated:
        #    if request.user.role.type == 'admin':
        #        return True
        #    elif request.user.role.type == 'staff' and request.method in list(permissions.SAFE_METHODS) + ['POST']:
        #        return True
        #    elif request.user.role.type == 'user' and request.method in permissions.SAFE_METHODS:
        #        return True
        #return False
    def has_object_permission(self, request, view, obj):
         # Allow admin to perform any action
        if request.user.role.type == 'admin':
            return True
        # Allow task owner to update or delete the task
        if request.user == obj.username:
            return True
        # Allow authenticated users to retrieve tasks
        return request.method in permissions.SAFE_METHODS
