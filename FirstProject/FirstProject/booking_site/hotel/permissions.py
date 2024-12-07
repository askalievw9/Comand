from rest_framework import permissions


class CheckStatus(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False


# class UpdateStatus(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):


class CheckReview(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return False
        return True


class CheckReservation(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.reservation_status == obj.свободен:
            return True
        return False


# class CheckNumber(permissions.BasePermission):
#     def has_permission(self, request, view):


# class Unique(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):


class Reservation(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return False
        return True
