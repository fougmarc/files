from rest_framework import viewsets
from sendfiles.models import *
from sendfiles.serializers import *
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework_files.viewsets import ImportExportModelViewSet
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response


class FileViewSet(viewsets.ModelViewSet):
    

    queryset = File.objects.all()
   
    serializer_class = FileSerializer
    
    def create(self, request):
       print("la requete est ..... !!!::",request)
       serializer_class = FileSerializer(data=request.data)
       if 'file' not in request.FILES or not serializer_class.is_valid():
           return Response(status=status.HTTP_400_BAD_REQUEST)
       else:
           handle_uploaded_file(request.FILES['file'])
           return Response(status=status.HTTP_201_CREATED)
    
    def handle_uploaded_file(f):
        with open(f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
    

class UserViewSet(viewsets.ModelViewSet):

    queryset =  User.objects.all()
    serializer_class =  UserSerializer
    def post(self, request):
        serializer = serializer.HelloSerializer(data=request.data)
        return Response()
