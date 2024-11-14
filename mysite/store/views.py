from rest_framework import viewsets, generics, status, permissions
from rest_framework.pagination import PageNumberPagination

from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import RoomFilter, HotelFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from .permissions import CheckOwner, CheckCRUD,\
    CheckOwnerHotel, CheckRoom, CheckBooking,\
    CheckReview,CheckRoomOwner, CheckBookUser, CheckImages


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 5


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers


class UserProfileSimpleViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSimpleSerializers


class HotelListViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = HotelFilter
    search_fields = ['hotel_name']
    ordering_fields = ['start']
    permission_classes = [CheckCRUD]
    permission_classes = [permissions.IsAdminUser]
    pagination_class = LargeResultsSetPagination


class HotelDetailViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializers
    permission_classes = [CheckCRUD, CheckOwnerHotel]


class HotelImageViewSet(viewsets.ModelViewSet):
    queryset = HotelImage.objects.all()
    serializer_class = HotelImageSerializers
    permission_classes = [CheckImages]


class RoomListViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomListSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = RoomFilter
    search_fields = ['room_number']
    ordering_fields = ['room_price']
    permission_classes = [CheckRoomOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RoomDetailViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializers
    filter_backends = [DjangoFilterBackend]
    permission_classes = [CheckRoom,CheckRoomOwner]


class RoomImageViewSet(viewsets.ModelViewSet):
    queryset = RoomImage.objects.all()
    serializer_class = RoomImageSerializers


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    permission_classes = [permissions.IsAuthenticated, CheckOwner, CheckReview]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers
    permission_classes = [CheckBooking, CheckBookUser]

