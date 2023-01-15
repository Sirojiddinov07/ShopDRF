from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from django.contrib.auth.models import User

from .product_view import StandardResultsSetPagination
from .serializers import *
# Create your views here.
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.hashers import make_password
from rest_framework import status, generics
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



@api_view(['POST'])
def registerUser(request):
    data = request.data
    try:
        user = User.objects.create(
            first_name=data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )

        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserProfile(request):
    user = request.user
    serializer = UserSerializerWithToken(user, many=False)

    data = request.data
    user.first_name = data['name']
    user.username = data['email']
    user.email = data['email']

    if data['password'] != '':
        user.password = make_password(data['password'])

    user.save()

    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)




@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)




@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUserById(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUser(request, pk):
    user = User.objects.get(id=pk)

    data = request.data

    user.first_name = data['name']
    user.username = data['email']
    user.email = data['email']
    user.is_staff = data['isAdmin']

    user.save()

    serializer = UserSerializer(user, many=False)

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteUser(request, pk):
    userForDeletion = User.objects.get(id=pk)
    userForDeletion.delete()
    return Response('User was deleted')





# Story, Blogs, BlogReview
class BlogsView(generics.ListAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer
    pagination_class = StandardResultsSetPagination




@api_view(['GET'])
def searchBlog(request):
    query = request.query_params.get('keyword')
    if query == None:
        query = ''

    blogs = Blogs.objects.filter(
        name__icontains=query).order_by('-createdAt')
    serializer = BlogsSerializer(blogs, many=True)
    return Response({'products': serializer.data} )



@api_view(['GET'])
def getBlog(request, pk):
    blog = Blogs.objects.get(id=pk)
    serializer = BlogsSerializer(blog, many=False)
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAdminUser])
def createBlog(request):
    user = request.user
    data = request.data


    blog = Blogs.objects.create(
        header=data['header'],
        text=data['text'],
        img=data['img'],

    )

    serializer = BlogsSerializer(blog, many=False)
    return Response(serializer.data)



@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateBlog(request, pk):
    data = request.data
    blog = Blogs.objects.get(id=pk)

    blog.header = data['header']
    blog.text = data['text']
    blog.img = data['img']


    blog.save()

    serializer = BlogsSerializer(blog, many=False)
    return Response(serializer.data)




@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteBlogs(request, pk):
    blog = Blogs.objects.get(id=pk)
    blog.delete()
    return Response('Blog Deleted')




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_story(request):
    story = Story.objects.last()
    serializer = StorySerializer(story, many=False)
    return Response(serializer.data)
