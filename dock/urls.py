from django.urls import path, include
from .views import *


urlpatterns = [
    path('create-dockerfile/', CreateDockerfile.as_view(), name="create-dockerfile"),
    path('get-all-dockerfiles/', GetAllDockerfiles.as_view(), name="get-all-dockerfiles"),
    path('get-dockerfile/<int:pk>/', GetDockerfile.as_view(), name="get-dockerfile"),
    path('update-dockerfile/<int:pk>/', UpdateDockerfile.as_view(), name="update-dockerfile"),
    path('delete-dockerfile/<int:pk>/', DeleteDockerfile.as_view(), name="delete-dockerfile"),
    path('test-dockerfile/', TestDockerfile.as_view(), name="test-dockerfile")
]
