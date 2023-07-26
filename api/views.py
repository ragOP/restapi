from django.shortcuts import render
from h11 import Response
from rest_framework import viewsets,permissions
from api.models import Company,Employee
from api.serializers import CompanySerializers,EmployeeSerializers
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSignupSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status




# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializers


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializers
    
    permission_classes = [IsAuthenticated]

    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializers(companies, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        name = request.data.get('name')

        # Check for existing employees with the same name
        if Employee.objects.filter(name=name).exists():
            return Response({'error': 'Employee with the same names already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)
    
class UserSignupView(APIView):
    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    