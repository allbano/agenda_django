"""
This module defines the Category model for the contact app.
"""
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    """
    Represents a category of contacts.
    
    Attributes:
        name (str): The name of the category.
    """
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name_plural = "Categories"  # Used for the admin plural name
        verbose_name = "Category"  # Used for the admin singular name
    
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100,blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254,blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True,upload_to="contact/pictures/%Y/%m/%d")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
        )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
