# WORK -> Auth class
# REQUIREMENTS -> null
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import exception_handler

from KHATF.FUNCTIONS import token_isvalid


class auth(IsAuthenticated):
    def has_permission(self, request, view):
        if token_isvalid(request):
            return True
        else:
            return False


# def custom_exception_handler(exc, context):
#     # Call REST framework's default exception handler first,
#     # to get the standard error response.
#     response = exception_handler(exc, context)
#
#     # Now add the HTTP status code to the response.
#     if response is not None:
#         response.data['status_code'] = response.status_code
#         response.data['id'] = ""
#         response.data['asd'] = response.detail
#     return response