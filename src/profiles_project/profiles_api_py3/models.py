from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    """Customize Django default User Manager class"""

    def create_user(self,email,name,password=None):
        """Create a User Profile Object"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self,email,name,password):
        """ Create a super user profile object """

        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user
    


class UserProfile (AbstractBaseUser, PermissionsMixin) :
    """ This class will represent the "user profile" inside our system """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ a helper function to retrieve fullname from user """
        
        return self.name
    
    def get_short_name(self):
        """ a helper function to retrieve user short name """

        return self.name
    
    def __str__(self):
        """ Use to custom formating of object representation as a string """
        return self.email

class ProfileFeedItem(models.Model):
    """Profile Status Update"""

    user_profile = models.ForeignKey('UserProfile',on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a String """
        return self.status_text

