from django.shortcuts import render
from .models import Student
from .serializer import StudentSerialzers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.mixins import (
    ListModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
)
from rest_framework.generics import GenericAPIView

# using view

# @method_decorator(csrf_exempt, name='dispatch')
# class StudentView(View):
#     def post(self, request, *args, **kwargs):
#         db = request.body
#         print(db)
#         db1 = json.loads(db)
#         serial = StudentSerialzers(data=db1)
#         if serial.is_valid():
#             serial.save()
#         return JsonResponse({"status": "success", "data": serial.data})

#     def put(self, request):
#         db = request.body
#         db1 = json.loads(db)
#         id = db1.get('id')
#         stu = Student.objects.get(pk=id)
#         serial = StudentSerialzers(stu, data=db1,partial=True)
#         if serial.is_valid():
#             serial.save()
#         return JsonResponse({"status": "success", "data": serial.data})


#     def delete(self, request):
#         db = request.body
#         db1 = json.loads(db)
#         id = db1.get('id')
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return JsonResponse({"status": "success"})

#     def get(self, request):
#         stu = Student.objects.all()
#         serial = StudentSerialzers(stu,many=True)
#         return JsonResponse({"status": "success", "data": serial.data})


# using api view rest framework
# class StudentView(APIView):
#     def post(self, request, format=None):
#         serial = StudentSerialzers(data=request.data)
#         if serial.is_valid():
#             serial.save()
#         else:
#             return Response(serial.errors)
#         return Response(serial.data)

#     def put(self, request, pk, format=None):
#         id = pk
#         print(id)
#         stu = Student.objects.get(pk=id)
#         serial = StudentSerialzers(stu, data=request.data)
#         if serial.is_valid():
#             serial.save()
#         else:
#             return Response(serial.errors)

#         return Response(serial.data)

#     def delete(self, request, pk, format=None):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response("del")

#     def get(self, request, pk=None, format=None):
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(pk=id)
#             serial = StudentSerialzers(stu)
#             return Response(serial.data)

#         else:
#             stu = Student.objects.all()
#             serial = StudentSerialzers(stu, many=True)
#             return Response(serial.data)


# genric view and modelmixin
# class StudentLC(GenericAPIView,ListModelMixin,CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerialzers

#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)

# class StudentUDR(GenericAPIView,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerialzers

#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)

#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)

#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)


# Modelviewset
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import (
    IsAdminUser,
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    DjangoModelPermissions
)


class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzers
    # authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions]
