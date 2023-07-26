from rest_framework import serializers
from api.models import Company, Employee
from .models import CustomUser


class CompanySerializers(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()

    class Meta:
        model = Company
        fields = "__all__"


class EmployeeSerializers(serializers.HyperlinkedModelSerializer):
    employee_id = serializers.ReadOnlyField()

    class Meta:
        model = Employee
        fields = "__all__"


class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'phone_number', 'first_name', 'last_name')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user
