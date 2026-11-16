from django.db import models

class User(models.Model):
    login = models.CharField('Логін',max_length=15)
    password = models.CharField('Пароль',max_length=15)
    first_name = models.CharField("Ім'я",max_length=15)
    last_name = models.CharField("Прізвише",max_length=15)
    email = models.EmailField('Електронна пошта', max_length=30)
    admin = models.BooleanField('Адмін', default=False)

    def __str__(self):
        return f"Користувач {self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'

