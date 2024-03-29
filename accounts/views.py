from django.shortcuts import render
from rest_framework import serializers, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
MIN_LENGTH = 8
# Create your views here.
@api_view(["POST",])
def logout_user(request):
    if request.method == "POST":
        request.user.auth.token.delete()
        return Response({"Message": "Siz saytdan chiqdingiz, endi qayta login qiling"}, status=status.HTTP_200_OK)
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=MIN_LENGTH,
        error_messages={
            "min_length": f"Parolngiz {MIN_LENGTH} dan ko'proq bo'lishi kerak"
        }
    )
    password2 = serializers.CharField(
        write_only=True,
        min_length=MIN_LENGTH,
        error_messages={
            "min_length": f"Parolngiz {MIN_LENGTH} dan ko'proq bo'lishi kerak"
        }
    )
    class Meta:
        model = User
        fields = "__all__"
    def vaidate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Parolingiz bir-biriga teng emas iltimos tekshirib qaytadan yozing")
        return data
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
