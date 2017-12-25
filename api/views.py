from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import CompanySerializer
from billing.models import Company


# Create your views here.
class CompanyList(APIView):
    serializer_class = CompanySerializer

    def get(self, request, format=None):
        queryset = Company.objects.all()
        response = self.serializer_class(queryset, many=True)
        return Response(response.data)

    def post(self, request, format=None):
        response = self.serializer_class(data=request.data)
        if response.is_valid():
            response.save()
            return Response(response.data, status=status.HTTP_201_CREATED)
        return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)


class CompaniList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
