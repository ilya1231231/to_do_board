from django.db import models

class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.CharField('Описание', max_length=1024)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name ='Задача'
        verbose_name_plural = 'Задачи'

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class UTask(models.Model):
    u_title = models.CharField('Название', max_length=50, null=True, blank=True)
    u_task = models.CharField('Описание', max_length=1024, null=True, blank=True )
    object_id = models.PositiveIntegerField(default=0)


    def __str__(self):
        return str(self.u_title)


    class Meta:
        verbose_name ='Задача пользователя'
        verbose_name_plural = 'Задачи пользователя'


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    avatar = models.ImageField('Аватар', upload_to='profile/', blank=True, null=True)
    first_name = models.CharField('Имя', max_length=50, blank=True, null=True)
    second_name = models.CharField('Фамилия', max_length=50, blank=True, null=True)
    worker_type = models.CharField('Должность', max_length=50, default='NULL', blank=True, null=True)
    taked_tasks_qty = models.PositiveIntegerField('Взято заданий', default=0, blank=True, null=True)
    u_individual_task = models.ManyToManyField(UTask, blank=True, related_name='related_utask')



    def __str__(self):
        return self.first_name


    #def save(self, *args, **kwargs):
       # super().save(*args, **kwargs)
        #self.slug = '{}{}'.format(self.user_id, self.first_name)

    #def get_absolute_url(self):
        #return reverse('profile-detail', kwargs={'name':self.user.username})


    class Meta:
        verbose_name ='Профиль'
        verbose_name_plural = 'Профили'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    '''Создание профиля пользователя при регистрации'''
    if created:
        Profile.objects.create(user=instance)


@receiver
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
