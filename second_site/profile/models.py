from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    avatar = models.ImageField('Аватар', upload_to='profile/', blank=True, null=True)
    first_name = models.CharField('Имя', max_length=50)
    second_name = models.CharField('Фамилия', max_length=50)


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