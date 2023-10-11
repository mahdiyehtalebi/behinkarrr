from rest_framework import serializers
from behinkar.models import adtitle
#class adtitleserializer(serializers.Serializer):
 #   company_name = serializers.CharField(max_length=150)
  #  state = serializers.CharField(max_length=50)
   # Description = serializers.CharField()

class adtitleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=adtitle
        fields='__all__'