from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField() #to get id of object models
    name = serializers.CharField(max_length=30)
    roll_num = serializers.IntegerField()
    city = serializers.CharField(max_length=30)