
from rest_framework import serializers


from .models import User, Todo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'address', 'age']

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=30, write_only=True)
    confirm_password = serializers.CharField(max_length=30, write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'address', 'password', 'confirm_password', 'age']

    def create(self, validated_data): 
        user = User.objects.create(
            username=validated_data['username'], 
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            address=validated_data['address']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'confirm_password': "Пароли не совпадают"})
        if len(attrs['password']) < 8:
            raise serializers.ValidationError({'password': "Минимум 8 символов"})
        
        return attrs
    
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
    
