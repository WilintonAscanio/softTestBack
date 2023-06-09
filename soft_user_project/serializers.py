from rest_framework import serializers

from .models import SoftUserProject

class SoftUserProjectSerializer(serializers.ModelSerializer):
    class Meta: 
         model = SoftUserProject
         fields = ('id', 'name', 'email', 'date', 'created_at' )
         read_only_fields = ('created_at',)
   