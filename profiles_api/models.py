from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models.expressions import Value


# Create your models here.
class UserProfileManager(BaseUserManager):
    """Manger for user profiles ( UserProfile() )"""
    
    def CreateUser(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password) #set_password automatically encripts this data
        user.save(using=self._db)

        return user
    
    def CreateSuperUser(self, email, name, password):
        """Create and save new super user with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user




class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system""" #docstring
    
    email = models.EmailField(max_length=255, unique=True) 
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True) #determines whether a users profile is activated or not, by default it is true.
    is_staff = models.BooleanField(default=False) #determines whether a user is a staff, by default it is false.
    

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def GetFullName(self):
        """Retrieve Full Name of User"""
        return self.name

    def GetShortName(self):
        """Retrieve Short Name of User"""
        return self.name

    def __str__(self):
        """Return string representation of our User"""
        return self.email