from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible


from django.db import models

# Create your models here.
@python_2_unicode_compatible
class Categories(models.Model):
	title = models.CharField(max_length=200)
	def __str__(self):
		return self.title

@python_2_unicode_compatible
class Items(models.Model):
	category = models.ForeignKey(Categories,on_delete=models.CASCADE )
	item_title = models.CharField(max_length=200)
	item_short_description = models.CharField(max_length=200)
	item_description = models.CharField(max_length=200)
	item_seller = models.CharField(max_length=200)
	item_menhaj = models.CharField(max_length=200)
	item_price = models.IntegerField(default=0)
	item_off = models.IntegerField(default=0)
	item_image = models.FileField(null = True , blank = True )
	
	def __str__(self):
		return self.item_title
		
@python_2_unicode_compatible
class UsersEmails(models.Model):
	user_email = models.CharField(max_length=200)
	
	def __str__(self):
		return self.user_email
	