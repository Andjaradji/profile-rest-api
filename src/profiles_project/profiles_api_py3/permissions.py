from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """ Allow User to edit their own profile """

    def has_object_permission(self, request,view, obj):
        """ Check User who is trying edit their own profie. """

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id

class PostOwnStatus(permissions.BasePermission):
    """ Allow User to have access to post their own status """

    def has_object_permission (self, request, view, obj):
        """ Checks the User is Trying to Update Their Own Status """

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile.id == request.user.id
        