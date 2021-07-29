from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

from .managers import CustomUserManager
# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    # required
    email = models.EmailField(_("Email address"), max_length=255, unique=True)

    # optional
    first_name = models.CharField(_("First name"), max_length=100, blank=True)
    last_name = models.CharField(_("Last name"), max_length=100, blank=True)
    country = CountryField()
    phone = models.CharField(_("Phone number"), max_length=70, blank=True)
    bio = models.TextField(_("About me"), blank=True)

    # user status
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    created = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated at"), auto_now=True)
    last_login = None

    USERNAME_FIELD = 'email' # Used for authentication
    objects = CustomUserManager() # model manager

    # methods
    def __str__(self):
        return self.full_name
    
    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        return self.email
    