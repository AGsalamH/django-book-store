import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model
from core.utils import unique_slug_generator
from .managers import ProductManager
# Create your models here.

# Current active AUTH_USER_MODEL
# cuz later im gonna create my custom user model
User = get_user_model()


class Category(models.Model):
    id = models.UUIDField(_('ID'), auto_created=True,
                          primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_('Category'), max_length=100, unique=True, error_messages={
        'unique': _('This category already exists!'),
        'required': _('Category name is required.'),
        'max_length': _('Please enter a shorter category name (max 100 letters).'),
    })
    slug = models.SlugField(_('slug'), max_length=255, unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        db_table = 'categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = unique_slug_generator(self)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("category", args=[self.slug])
    

    @property
    def title(self):
        return self.name


class Product(models.Model):
    id = models.UUIDField(_('ID'), auto_created=True,
                          primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(
        'store.Category', on_delete=models.SET_NULL, null=True,  related_name='products')
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    author = models.CharField(
        _("Book author"), max_length=255, default='Admin')
    description = models.TextField(blank=True)
    image = models.ImageField(
        _('product image'), upload_to='products', default='products/default.png')
    slug = models.SlugField(unique=True, max_length=255)
    price = models.DecimalField(_("price"), max_digits=100, decimal_places=2)

    in_stock = models.BooleanField(_("stock status"), default=True)
    is_active = models.BooleanField(_("active status"), default=True)

    objects = models.Manager()
    products = ProductManager()

    class Meta:
        db_table = 'products'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = unique_slug_generator(self)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])
    

    @property
    def title(self):
        return self.name
