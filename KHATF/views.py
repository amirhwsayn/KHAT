# Create your views here.
from rest_framework import generics
from rest_framework import status, exceptions
from rest_framework.response import Response
from rest_framework.views import APIView
from .FUNCTIONS import *
from .Serializers import *
# WORK -> Create Token
# REQUIREMENTS -> HEADER : email
from .utils import auth


class send_token(APIView):
    def get(self, request):
        if 'email' in request.headers:
            email = request.headers['email']
            token = SendToken(email)
            return Response(token, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# WORK -> Register Admin Via Valid Token
# REQUIREMENTS -> HEADER : code , token  &&  BODY_form-data : Admin Data
class register_admin(generics.CreateAPIView):
    permission_classes = (auth,)
    serializer_class = SERIadmin

    def handle_exception(self, exc):
        respons = ''
        if isinstance(exc, exceptions.NotAuthenticated):
            respons = {"detail": "کد راستی آزمایی نا معتبر"}
        elif isinstance(exc, exceptions.ValidationError):
            respons = {"detail": "کابر دیگری با این نام کاربری وجود دارد"}
        return Response(respons)
