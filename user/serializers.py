from dataclasses import fields
from .models import ApiUsers
from rest_framework import serializers



class Apiuserserializers(serializers.ModelSerializer):
    class Meta:
        model=ApiUsers
        # fields={'username','password'}
        fields = '__all__'