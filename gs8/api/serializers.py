from rest_framework import fields, serializers, validators
from .models import Student




class StudentSerializer(serializers.ModelSerializer):
    # Validators
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name should start with R')

    name = serializers.CharField(validators=[start_with_r])
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
  

    # Fieldlevel validation
    def validate_roll(self, value):
        if value >=200:
            raise serializers.ValidationError('Seat Full')
        return value

    # City level validation
    def validate(self, data):
        nam = data.get('name')
        ct = data.get('city')
        if nam.lower() == 'lalita' and ct.lower() !='thane':
            raise serializers.ValidationError('City must be Thane')
        return data


       