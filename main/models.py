from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class BlogPost(models.Model):
    email = models.EmailField('Email', max_length=50)
    title = models.CharField('Заголовок', max_length=250)
    message = models.TextField('Повідомлення')
    date = models.DateField('Дата публікації')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пости'


class MyUser(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
