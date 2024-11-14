from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user_role', 'email', 'password']


class UserProfileSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name','last_name']


class HotelListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name', 'description']


class HotelDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['hotel_name', 'owner', 'description', 'country', 'city', 'address',
                  'start', 'hotel_video', 'created_date']


class HotelImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = '__all__'


class RoomListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['hotel_room', 'room_number', 'room_description']


class RoomDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['room_number', 'hotel_room', 'room_type',
                  'room_status', 'room_price', 'all_inclusive', 'room_description']


class RoomImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = '__all__'


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['user_name', 'hotel', 'text', 'stars', 'parent']


class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['user_book',  'hotel_book', 'room_book',
                  'check_in', 'check_out', 'status_book']

