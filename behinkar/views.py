from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from behinkar.models import adtitle
from behinkar.serializers import adtitleModelSerializer
from rest_framework import generics,mixins
from rest_framework import permissions

class GETAPI(APIView):
    def get(self,request):
        query=adtitle.objects.all()
        serializers=adtitleModelSerializer(query,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def alldata(request):
    if request.method == 'GET':
        queri = adtitle.objects.all().order_by('-create_at')
        serilizer = adtitleModelSerializer(queri, many=True)
        return Response(serilizer.data, status.HTTP_200_OK)

@api_view(['POST'])
def setdata(request):
    if request.method == 'POST':
        serializer = adtitleModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class mixinsAPI(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset =adtitle.objects.order_by('create_at').all()
    serializer_class = adtitleModelSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

class mixinsAPIVIEW(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = adtitle.objects.order_by('create_at').all()
    serializer_class = adtitleModelSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)
    def put(self,request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return self.delete(request,pk)

