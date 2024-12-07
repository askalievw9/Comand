from .views import *
from django.urls import path


urlpatterns = [
    # path('register/', RegisterView.as_view(), name='register'),
    # path('login/', CustomLoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),

    path('', HotelListViewSet.as_view({'get': 'list', 'post': 'create'}), name='hotel_list'),
    path('<int:pk>/', HotelDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                  'delete': 'destroy'}), name='hotel_detail'),

    path('room/', RoomListViewSet.as_view({'get': 'list', 'post': 'create'}), name='room_list'),
    path('room/<int:pk>/', RoomDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                      'delete': 'destroy'}), name='room_detail'),

    path('users/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='user_list'),
    path('users/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                        'delete': 'destroy'}), name='user_detail'),

    path('review/', ReviewViewSet.as_view({'get': 'list', 'post': 'create'}), name='review_list'),
    path('review/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                    'delete': 'destroy'}), name='review_detail'),

    path('hotel_photos/', HotelImageViewSet.as_view({'get': 'list', 'post': 'create'}), name='hotel_image_list'),
    path('hotel_photos/<int:pk>/', HotelImageViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                               'delete': 'destroy'}), name='hotel_image_detail'),

    path('room_photos/', RoomImageViewSet.as_view({'get': 'list', 'post': 'create'}), name='room_image_list'),
    path('room_photos/<int:pk>/', RoomImageViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                             'delete': 'destroy'}), name='room_image_detail'),

]