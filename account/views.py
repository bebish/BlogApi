from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer

# Create your views here.
class UserRegistration(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data) # композиция, сильная связь, обьект создан внутри класса
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Account is created', status=200) 

    