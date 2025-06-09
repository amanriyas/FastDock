from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *
from .ai_utils import generate_dockerfile

# Create your views here.

class CreateDockerfile(APIView):
    def post(self, request):
        serializer = DockerfileRequestSerializer(data=request.data)
        if serializer.is_valid():
            dockerfile = generate_dockerfile(serializer.validated_data['stack_description'], serializer.validated_data['production_ready'])
            serializer.validated_data['generated_dockerfile'] = dockerfile
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetAllDockerfiles(APIView):
    def get(self, request):
        dockerfiles = DockerfileRequest.objects.all()
        serializer = DockerfileRequestSerializer(dockerfiles, many=True)
        return Response(serializer.data)


class GetDockerfile(APIView):
    def get(self, request, pk):
        dockerfile = DockerfileRequest.objects.get(pk=pk)
        serializer = DockerfileRequestSerializer(dockerfile)
        return Response(serializer.data)


class UpdateDockerfile(APIView):
    def patch(self, request, pk):
        dockerfile = DockerfileRequest.objects.get(pk=pk)
        serializer = DockerfileRequestSerializer(dockerfile, data=request.data, partial=True)
        if serializer.is_valid():
            dockerfile.generated_dockerfile = generate_dockerfile(serializer.validated_data.get('stack_description', dockerfile.stack_description), serializer.validated_data.get('production_ready', dockerfile.production_ready))
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteDockerfile(APIView):
    def delete(self, request, pk):
        dockerfile = DockerfileRequest.objects.get(pk=pk)
        dockerfile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TestDockerfile(APIView):
    def get(self, request):
        dockerfile = generate_dockerfile("Node.js", True)
        return Response(dockerfile)
        
