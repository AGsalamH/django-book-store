from django.contrib.auth import get_user_model
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def _create_user(self, email=None, password=None, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
    
        if not password:
            raise ValueError('The given password must be set')

        user = self.model(
            email = self.normalize_email(email),
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        
        if extra_fields.get('is_staff') is True:
            raise ValueError(_('A user can NOT have is_staff=True'))
        if extra_fields.get('is_superuser') is True:
            raise ValueError(_('A user can NOT have is_superuser=True'))
        
        return self._create_user(email=email, password=password, **extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('A superuser must have is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('A user must have is_superuser=True'))
        
        return self._create_user(email=email, password=password, **extra_fields)

    def create_staffuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('A staff member must have is_staff=True'))
        if extra_fields.get('is_superuser') is True:
            raise ValueError(_('A staff member cant NOT have is_superuser=True'))
        
        return self._create_user(email=email, password=password, **extra_fields)
