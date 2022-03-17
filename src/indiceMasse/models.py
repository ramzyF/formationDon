from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
# Create your models here.

class MyPatientManager(BaseUserManager):
  def create_user(self, email, name, tel_number, city, password=None):
    if not email:
      raise ValueError('Email is required')
    if not name:
      raise ValueError('Patient name is required')
    if not tel_number:
      raise ValueError('Please provide an active phone number')
  
    user=self.model(
      email=self.normalize_email(email),
      name=name,
      tel_number = tel_number,
      city=city,
    )
    user.set_password(password)
    user.save(using=self._db)
    return user
  def create_superuser(self, email, name, tel_number, city,password=None):
    user = self.create_user(
      email=email,
      name=name,
      tel_number=tel_number,
      password=password,
      city = city
    )

    user.is_admin = True
    user.is_staff = True
    user.is_superuser = True
    user.save(using=self._db)
    return user
  
class Patient(AbstractBaseUser):
  email = models.EmailField(verbose_name=_('email adress'), max_length= 68, unique=True)
  name = models.CharField(verbose_name=_("nom du patient") , max_length=200, null=True)
  tel_number = models.CharField(_("numéro de tel"),max_length=13, null=True)
  city = models.CharField(verbose_name=_('City'),max_length=100)
  date_joined = models.DateTimeField(_("d"),auto_now_add=True)
  last_login = models.DateTimeField(_('last login'), blank=True, null=True, auto_now=True)
  is_admin = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)

  
  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = ['name', 'tel_number', 'city']
  
  objects = MyPatientManager()
  
  def __str__(self):
    return self.name
  
  def has_perm(self, perm, obj=None):
    return True
  
  def has_module_perms(self, app_label):
    return True
  
''' class Patient(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,)
  name = models.CharField(max_length=200, null=True)
  tel_number = models.CharField(max_length=13, null=True)
  city= models.CharField(max_length=100)
 '''
