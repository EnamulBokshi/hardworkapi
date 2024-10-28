from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.db.models import Sum


#RestFramework
from rest_framework import status
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
from rest_framework_simplejwt.tokens import RefreshToken

from drf_yasg import openapi
from drf_yasg.utils import  swagger_auto_schema


from datetime import datetime

import json
import random


from api import serializer as api_serializer
from api import models as api_models



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = api_serializer.MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = api_models.User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = api_serializer.RegisterSerializer

class Profileview(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class  = api_serializer.ProfileSerializer

    def get_object(self):
        user_id = self.kwargs['user_id']
        user = api_models.User.objects.get(id = user_id)
        profile  = api_models.Profile.objects.get(user = user)
        return profile

class PostListAPIView(generics.ListAPIView):
    serializer_class  = api_serializer.PostSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return api_models.Post.objects.filter(status = "Active")
class PostListAllAPIView(generics.ListAPIView):
    serializer_class  = api_serializer.PostSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return api_models.Post.objects.all().order_by("-id")
    
class PostDetailsAPIView(generics.RetrieveAPIView):
    serializer_class = api_serializer.PostSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        id = self.kwargs['id']
        post = api_models.Post.objects.get(id = id)
        post.view +=1
        post.save()
        return post

# class PostDeleteAPIView(generics.DestroyAPIView):
#     serializer_class = api_serializer.PostSerializer
#     permission_classes = [AllowAny]


#     def get_object(self):
#         id = self.kwargs['id']
#         post = api_models.Post.objects.get(id = id)
#         post.delete()
#         return Response({"message":"Post deleted successfully"},status=status.HTTP_200_OK)

class PostFeaturedAPIView(generics.ListAPIView):
    serializer_class  = api_serializer.PostSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        return api_models.Post.objects.filter(status = "Featured")
#Gallery 
class GalleryCreate(generics.CreateAPIView):
    queryset = api_models.Gallery.objects.all()
    serializer_class = api_serializer.GallerySerializer
    permission_classes = [AllowAny]

    # def gallery_create(request):
    #     if request.method == "POST":
    #         return JsonResponse({"message": "POST request received"}, status=201)
    #     return JsonResponse({"error": "Method not allowed"}, status=405)


    # def create(self, request, *args, **kwargs):
    #     title = request.data.get("title")
    #     image = request.data.get("image")
    #     status = request.data.get("status")
    #     item = api_models.Gallery.objects.create(
    #         title = title,
    #         image = image,
    #         status = status
    #     )
    #     return Response({"message":"Gallery Item added successfully"},status = status.HTTP_201_CREATED)

class GalleryAPIView(generics.ListAPIView):
    serializer_class = api_serializer.GallerySerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        return api_models.Gallery.objects.filter(status = "Active")
    

class GellerySingleItemAPIVew(generics.ListAPIView):
    serializer_class = api_serializer.GallerySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        id = self.kwargs['id']
        return api_models.Gallery.objects.filter(id = id)

class GalleryDeleteView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = api_models.Gallery.objects.all()
    serializer_class = api_serializer.GallerySerializer
    permission_classes = [AllowAny]
    # lookup_field = 'id'
    def get_object(self):
        itemId = self.kwargs['item_id']
        item = api_models.Gallery.objects.get(id = itemId)
        return item
    
    def get_queryset(self):
        return self.get_object()
        
    def destroy(self, request, *args, **kwargs):
        post_instance = self.get_object()
        post_instance.delete()
        return Response({"message":"Item Deleted successfully"},status = status.HTTP_200_OK)


#DashBoard

class DashboardPostLists(generics.ListAPIView):
    serializer_class = api_serializer.PostSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        user = api_models.User.objects.get(id = user_id)
        return api_models.Post.objects.filter(user = user).order_by("-id")
class DashboardPostCreateAPIView(generics.CreateAPIView):
    serializer_class = api_serializer.PostSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
    #    print(request.data)
        user_id = request.data.get("user_id")
        title = request.data.get("title")
        image = request.data.get("image")
        text = request.data.get("text")
        tags = request.data.get("tags")
        post_status = request.data.get("post_status")

        user = api_models.User.objects.get(id = user_id)
        profile = api_models.Profile.objects.get(id = user_id)
        post = api_models.Post.objects.create(
            user=user,
            profile = profile,
            title = title,
            text = text,
            tags=tags,
            image = image,
            status = post_status
        )

        return Response({"message":"Post created successfully"},status = status.HTTP_201_CREATED)

class DashboardPostUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = api_serializer.PostSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        user_id = self.kwargs['user_id']
        post_id = self.kwargs['post_id']

        user = api_models.User.objects.get(id = user_id)
        post = api_models.Post.objects.get(id = post_id,user = user)

        return post
    
    def update(self, request, *args, **kwargs):
        post_instance = self.get_object()

        title = request.data.get("title")
        image = request.data.get("image")
        description = request.data.get("description")
        tags = request.data.get("tags")
        post_status = request.data.get("post_status")
        post_instance.title = title
        if image != "undefined":
            post_instance.image = image
        post_instance.description = description
        post_instance.tags = tags
  
        post_instance.post_status = post_status
        post_instance.save()

        return Response({"message":"Post updated successfully"},status = status.HTTP_200_OK)
    def destroy(self, request, *args, **kwargs):
       post_instance = self.get_object()
       post_instance.delete()
       return Response({"message":"Post Deleted successfully"},status = status.HTTP_200_OK)

# class DashboardGalleryAPIView(ge)
class DashboardGalleryAPIView(generics.ListAPIView):
    serializer_class = api_serializer.GallerySerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        return api_models.Gallery.objects.all()
# class DashBoardGalleryUpdate(generics.RetrieveUpdateDestroyAPIView):


class DashboardQuoteAPIView(generics.ListAPIView):
    serializer_class = api_serializer.QuoteSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        return api_models.Quote.objects.all()

class QuoteCreate(generics.CreateAPIView):
    serializer_class = api_serializer.QuoteSerializer
    permission_classes = [AllowAny]
    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        email = request.data.get('email')
        message = request.data.get('message')

        quote = api_models.Quote.objects.create(
            name = name,
            email = email,
            message = message
        )
        return Response({"message":"Qote Gotted"},status = status.HTTP_201_CREATED)

class QuoteDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = api_serializer.QuoteSerializer
    permission_classes  = [AllowAny]
    def get_object(self):
       id = self.kwargs['pk']
       q = api_models.Quote.objects.get(id = id)
       return q
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message":"Quote Deleted succesfully!!!"},status=status.HTTP_204_NO_CONTENT)