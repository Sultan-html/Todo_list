from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=50,
                                verbose_name='Имя пользвателя', 
                                unique=True)
    
    email = models.EmailField(verbose_name='Адрес электронной почты', unique=True)

    created_at = models.DateTimeField(auto_now=True,
    verbose_name='Дата регистрации')

    age = models.IntegerField(verbose_name='Возраст',
                              default=5)

    phone_number = models.CharField(max_length=25, verbose_name="номер телефона", null=True, blank=True)

    address = models.CharField(max_length=150, verbose_name="адрес проживания", null=True, blank=True)


    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = "Пользователи"

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(max_length=155, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    is_completed = models.BooleanField(default=False, verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/', verbose_name='Изображение') 

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = "Задачи"