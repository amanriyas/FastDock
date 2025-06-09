from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

# Create your views here.

class CreateDockerfile(APIView):
    def post(self, request):
        serializer = DockerfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetAllDockerfiles(APIView):
    def get(self, request):
        dockerfiles = Dockerfile.objects.all()
        serializer = DockerfileSerializer(dockerfiles, many=True)
        return Response(serializer.data)


class GetDockerfile(APIView):
    def get(self, request, pk):
        dockerfile = Dockerfile.objects.get(pk=pk)
        serializer = DockerfileSerializer(dockerfile)
        return Response(serializer.data)


class UpdateDockerfile(APIView):
    def put(self, request, pk):
        dockerfile = Dockerfile.objects.get(pk=pk)
        serializer = DockerfileSerializer(dockerfile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteDockerfile(APIView):
    def delete(self, request, pk):
        dockerfile = Dockerfile.objects.get(pk=pk)
        dockerfile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)