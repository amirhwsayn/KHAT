from rest_framework import serializers
from .models import *


class SERIclass(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = "__all__"


class SERIadmin(serializers.ModelSerializer):

    class Meta:
        model = Admin
        fields = [
            'id',
            'password',
            'email',
            'name',
            'profilePicture',
        ]
