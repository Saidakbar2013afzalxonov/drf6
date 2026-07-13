from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','first_name','last_name','email','age','created_at','phone_number']
        read_only_fields = ['id','created_at']