from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class Worker(models.Model):
    user = models.ForeignKey(User, verbose_name='Работник', on_delete=models.CASCADE)
    first_name = models.CharField('Имя', max_length=50, blank=True, null=True)
    second_name = models.CharField('Фамилия', max_length=50, blank=True, null=True)

    def __str__(self):
        return 'Работник: {} {}'.format(self.first_name, self.second_name)

class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.CharField('Описание', max_length=1024)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name ='Задача'
        verbose_name_plural = 'Задачи'

    # def get_model_name(self):
    #     return self.__class__.__name__.lower()


class UTask(models.Model):
    profile = models.ForeignKey('Profile', null=True, verbose_name='Профиль', on_delete=models.CASCADE,related_name='related_profile')
    u_title = models.CharField('Название', max_length=50, null=True, blank=True)
    u_task = models.CharField('Описание', max_length=1024, null=True, blank=True )



    def __str__(self):
        return str(self.u_title)


    class Meta:
        verbose_name ='Задача пользователя'
        verbose_name_plural = 'Задачи пользователя'


class Profile(models.Model):
    owner = models.OneToOneField('Worker', null=True, verbose_name='Владелец профиля', on_delete=models.CASCADE)
    avatar = models.ImageField('Аватар', upload_to='profile/', blank=True, null=True)
    worker_type = models.CharField('Должность', max_length=50, default='NULL', blank=True, null=True)
    first_name = models.CharField('Имя', max_length=50, blank=True, null=True)
    second_name = models.CharField('Фамилия', max_length=50, blank=True, null=True)
    taked_tasks_qty = models.PositiveIntegerField('Взято заданий', default=0, blank=True, null=True)
    u_individual_task = models.ManyToManyField(UTask, blank=True, related_name='related_utask')



    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        profile_data = self.u_individual_task.aggregate(models.Count('id'))
        self.taked_tasks_qty = profile_data['id__count']
        print(profile_data)
        super().save(*args, **kwargs)

    #def save(self, *args, **kwargs):
       # super().save(*args, **kwargs)
        #self.slug = '{}{}'.format(self.user_id, self.first_name)

    #def get_absolute_url(self):
        #return reverse('profile-detail', kwargs={'name':self.user.username})


    class Meta:
        verbose_name ='Профиль'
        verbose_name_plural = 'Профили'


@receiver(post_save, sender=Worker)
def create_user_profile(sender, instance, created, **kwargs):
    '''Создание профиля пользователя при регистрации'''
    if created:
        Profile.objects.create(owner=instance)


@receiver
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
