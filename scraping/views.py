from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView

from scraping.serializers import EmployeeSerializer


class CreateEmployeeView(CreateAPIView):
    serializer_class = EmployeeSerializer
