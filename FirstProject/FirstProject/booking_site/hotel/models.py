from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MaxValueValidator(110)], null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True, region='KG')

    STATUS_CHOICES = (
        ('simple', 'simple'),
        ('owner', 'owner')
    )

    user_status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='simple')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_address = models.CharField(max_length=64)
    description = models.TextField()
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=32)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    stars = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.hotel_name}, {self.country}'


class Room(models.Model):
    room_number = models.PositiveSmallIntegerField()
    rooms = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')

    TYPES_CHOICES = (
        ('люкс', 'люкс'),
        ('семейный', 'семейный'),
        ('одноком', 'одноком'),
        ('двухком', 'двухком')
    )

    room_types = models.CharField(max_length=16, choices=TYPES_CHOICES)

    RESERVATION_CHOICES = (
        ('свободен', 'свободен'),
        ('забронирован', 'забронирован'),
        ('занят', 'занят'),
    )

    reservation_status = models.CharField(max_length=16, choices=RESERVATION_CHOICES, default='свободен')
    room_price = models.PositiveIntegerField()
    room_description = models.TextField()
    all_inclusive = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.rooms}, {self.room_types}, {self.room_number}'


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_images')
    hotel_image = models.ImageField(upload_to='hotel_image/', null=True, blank=True)
    hotel_video = models.FileField(upload_to='vid/', verbose_name='Видео', null=True, blank=True)

class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_images')
    room_image = models.ImageField(upload_to='room_image/', null=True, blank=True)


class Review(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    text = models.TextField()
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='Рейтинг')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.author}, {self.hotel}, {self.stars}'


class Booking(models.Model):
    hotel_book = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_book = models.ForeignKey(Room, on_delete=models.CASCADE)
    user_book = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    chek_in = models.DateTimeField()
    chek_uot = models.DateTimeField()
    total_price = models.PositiveIntegerField(default=0)
    STATUS_BOOK_ROOM = (
        ('отменено', 'отменено'),
        ('подверждено', 'подверждено')
    )
    status_book = models.CharField(max_length=16, choices=STATUS_BOOK_ROOM)

    def __str__(self):
        return f'{self.user_book}, {self.hotel_book}, {self.room_book}, {self.status_book }'