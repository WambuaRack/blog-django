from rest_framework import serializers
from .models import *

class BlogSerializer(serializers.Serializer):
     class Meta:
         model=Blog
         fields="__all__"
         