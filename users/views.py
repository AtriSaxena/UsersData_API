from django.shortcuts import render,redirect
from .models import UsersData
from rest_framework import status 
from rest_framework.parsers import JSONParser
from django.db.models.functions import Concat
from django.db.models import Value
from users.serializers import UserDataSerializer
from rest_framework.response import Response 
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
import json


#API to get all user, and post user
class UsersAll(APIView):
    def get(self,request, format=None):
        if request.method=='GET' and 'name' in request.GET:
            name = request.GET.get('name')
            sortby = request.GET.get('sort')
            limit = request.GET.get('limit')
            page = request.GET.get('page')
            if limit is None:
                limit = 5
            queryset_list = UsersData.objects.annotate(fullname=Concat('first_name', Value(' '),'last_name'))
            if sortby is None:
                queryset_list = queryset_list.filter(fullname__contains=name)
            else:
                queryset_list = queryset_list.filter(fullname__contains=name).order_by(sortby)   #search user by name and sort 
            paginator = Paginator(queryset_list,limit) #Pagination 
            try:
                queryset = paginator.page(page)
            except PageNotAnInteger:
                queryset = paginator.page(1)
            except EmptyPage:
                queryset = paginator.page(paginator.num_pages) 
            users = []
            for user in queryset:
                users.append(user.id) #get user id of required users
            if sortby is None:
                query = UsersData.objects.filter(id__in=users) #get users data
            else:
                query = UsersData.objects.filter(id__in=users).order_by(sortby) #get users data  
            serializer = UserDataSerializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK) #return data
        else:
            queryset = UsersData.objects.all() #get all users if values are not set
            serializer = UserDataSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK) #Return users
                    
        
    def post(self,request,format=None):
        serializer = UserDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()   #save users data
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #Return error if data is not valid

#GET , PUT, DELETE for particular user
class UserDetails(APIView):
    def get_object(self,id):
        try:
            return UsersData.objects.get(id=id) 
        except UsersData.DoesNotExist:
            raise Http404
        
    def get(self, request, id, format=None):
        user = self.get_object(id) 
        serializer = UserDataSerializer(user)
        return Response(serializer.data)
        
    def put(self,request,id,format=None): #Update user
        user = self.get_object(id)
        serializer = UserDataSerializer(user,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(json.loads('{}'),status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request, id, format=None): #Delete use
        user = self.get_object(id)
        user.delete()
        return Response(json.loads('{}'),status=status.HTTP_200_OK)