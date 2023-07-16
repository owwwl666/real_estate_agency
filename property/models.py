from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    owner = models.CharField('ФИО владельца', max_length=200)
    owners_phonenumber = models.CharField('Номер владельца', max_length=20)
    owner_pure_phone = PhoneNumberField(region="RU", blank=True, verbose_name="Нормализованный номер владельца")
    new_building = models.BooleanField(blank=True, null=True, verbose_name="Новостройка")

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)
    likes = models.ManyToManyField(User, verbose_name="Кто лайкнул", related_name="user_likes", blank=True)
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class UserComplaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Кто жаловался")
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE,
                             verbose_name="Квартира,на которую пожаловались")
    text = models.TextField(max_length=500, verbose_name="Текст жалобы")


class Owner(models.Model):
    owner = models.CharField('ФИО владельца', max_length=200, db_index=True)
    owners_phonenumber = models.CharField('Номер владельца', max_length=20, db_index=True)
    owner_pure_phone = PhoneNumberField(region="RU", blank=True, verbose_name="Нормализованный номер владельца",
                                        db_index=True)
    possessions = models.ManyToManyField(Flat, verbose_name="Квартиры в собственности", related_name="owners")

    def __str__(self):
        return self.owner
