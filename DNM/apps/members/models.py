# coding=utf-8

from sorl.thumbnail import ImageField

from django.contrib.auth.models import *
from django.db import models
from django.contrib.auth import models as auth_models
import os

__author__ = 'eaura'

class Grad(models.Model):
    def __unicode__(self):
        return self.grad

    grad = models.CharField(max_length=200, verbose_name='Grad')
    order = models.SmallIntegerField(verbose_name='Order')

    def isGuest(self):
        if self.grad == u'Gäst':
            return True
        else:
            return False

    class Meta:
        ordering = ('order',)


class Title(models.Model):
    def __unicode__(self):
        return self.namn or u''
    styrelsePost = models.NullBooleanField(max_length=200, verbose_name=u'Styrelsepost')

    namn = models.CharField(max_length=200, verbose_name=u'Titel')

class MyUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = UserManager.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=False, is_active=True, is_superuser=False,
                          last_login=now, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        u = self.create_user(username, email, password, **extra_fields)
        u.is_staff = True
        u.is_active = True
        u.is_superuser = True
        u.save(using=self._db)
        return u

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Member(AbstractBaseUser, PermissionsMixin):
    # Link to the user model
    username = models.CharField(max_length=30, unique=True, db_index=True, verbose_name=u'Användarnamn')
    email = models.EmailField('E-post', max_length=254, unique=True)
    first_name = models.CharField(max_length=200, verbose_name=u'Förnamn')
    last_name = models.CharField(max_length=200, verbose_name='Efternamn')
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    # fodelsedatum = models.DateField('date of birth', blank=True, null=True)
    grad = models.ForeignKey(Grad, blank=False, default=1)
    title = models.ForeignKey(Title, blank=True, null=True, verbose_name=u'Titel')

    phone = models.CharField(max_length=200, blank=True, verbose_name=u'Telefonnummer')
    address = models.CharField(max_length=200, blank=True, verbose_name=u'Postadress')
    is_staff = models.BooleanField('staff status', default=False,
                                   help_text='Designates whether the user can log into this admin '
                                             'site.')
    is_active = models.BooleanField('active', default=True,
                                    help_text='Designates whether this user should be treated as '
                                              'active. Unselect this instead of deleting accounts.')

    image = ImageField(upload_to=get_image_path, blank=True, null=True,  verbose_name=u'Profilbild')
    diet  = models.CharField(max_length=500, blank=True, null=True, verbose_name=u'Diet')
    birthday = models.DateTimeField(verbose_name='Födelsetid',blank=False,null=True)


    def up_to_date(self):
        return self.birthday is not None

    def get_full_name(self):
        full_name = ''
        if self.title:
            full_name += ' '
            full_name += self.title.namn
        full_name += ' '
        full_name +=self.first_name +" "+self.last_name
        return full_name

    def get_short_name(self):
        return self.first_name

    objects = MyUserManager()

auth_models.User = Member

class Avec(models.Model):
    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=200, verbose_name=u'Namn')
    diet = models.CharField(max_length=200, verbose_name=u'Diet',null=True, blank=True)
    email = models.CharField(max_length=200, verbose_name=u'E-post')
    members  = models.ForeignKey(Member, blank=True, null=True, verbose_name=u'Avec')

# Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_save
from django.dispatch.dispatcher import receiver

@receiver(pre_save, sender=Member)
def delete_old_image(sender, instance, *args, **kwargs):
    if instance.pk:
        existing_image = Member.objects.get(pk=instance.pk)
        if instance.image and existing_image.image != instance.image:
            existing_image.image.delete(False)