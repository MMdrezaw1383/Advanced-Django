from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class UserManager(BaseUserManager):
    '''
    Custom user model manager
    '''
    def create_user(self,email,password,**extra_fields):
        ''' 
        Create and save user with fields
        '''
        if not email:
            raise ValueError(_("The email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user 
    
    def create_superuser(self,email,password,**extra_fields):
        '''
        Create and save super user
        '''
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("s_staff must be true"))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("is_superuser must be true"))
        
        return self.create_user(email,password,**extra_fields)
class User(AbstractBaseUser,PermissionsMixin):
    '''
    Custom User Model for our project 
    where email is the unique identifiers for authentications.
    '''
    email = models.EmailField(_("email"), max_length=254,unique=True)
    is_superuser = models.BooleanField(_("is_superuser"),default=False )
    is_staff = models.BooleanField(_("is staff"),default=False)
    is_active = models.BooleanField(_("is active"),default=True)
    #  is_verified = models.BooleanField(_("is verified"),default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    created = models.DateTimeField(_("created at"), auto_now_add=True)
    updated = models.DateTimeField(_("updated at"), auto_now=True)
    
    objects = UserManager()
    

class Profile(models.Model):
    user = models.ForeignKey("User", verbose_name=_("user"), on_delete=models.CASCADE)
    first_name = models.CharField(_("first_name"), max_length=50)
    last_name = models.CharField(_("last_name"), max_length=50)
    image = models.ImageField(_("image"), upload_to=None, height_field=None, width_field=None, max_length=None,blank=True,null=True)
    description = models.TextField(_("description"))
    
    created = models.DateTimeField(_("created at"), auto_now_add=True)
    updated = models.DateTimeField(_("updated at"), auto_now=True)
    
    
    def __str__(self):
        return self.user.email 
    
    
    
@receiver(post_save,sender=User)
def save_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
      