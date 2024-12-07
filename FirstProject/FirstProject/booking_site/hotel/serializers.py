from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }



class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number',]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['first_name', 'last_name']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['hotel_video', 'hotel_image']


class RoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['room_number', 'rooms', 'room_price']


class HotelListSerializer(serializers.ModelSerializer):
    rooms = RoomListSerializer(read_only=True, many=True)
    class Meta:
        model = Hotel
        fields = ['hotel_name', 'country', 'stars', 'rooms']


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['room_image', 'room']


class RoomDetailSerializer(serializers.ModelSerializer):
    room_images = RoomImageSerializer(read_only=True, many=True)

    class Meta:
        model = Room
        fields = ['room_number', 'rooms', 'room_images', 'room_price', 'room_types', 'reservation_status',
                  'room_description', 'all_inclusive']


class HotelDetailSerializer(serializers.ModelSerializer):
    hotel_images = HotelImageSerializer(read_only=True, many=True)
    rooms = RoomDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Hotel
        fields = ['owner', 'hotel_name', 'hotel_images', 'country', 'city', 'hotel_address', 'description', 'rooms', 'stars']