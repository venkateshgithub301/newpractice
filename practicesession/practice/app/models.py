from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class book(models.Model):
	name=models.CharField(max_length=100)
	author=models.OneToOneField(User,related_name='User')

def __str__(self):
	return self.name


class MultiBooks(models.Model):
	name=models.CharField(max_length=100)
	author=models.ForeignKey(User)
def __str__(self):
	return self.name


class MultiAuthorsandBooks(models.Model):
	name=models.CharField(max_length=100)
	author=models.ManyToManyField(User)

def __str__(self):
	return self.name