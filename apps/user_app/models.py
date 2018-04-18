from __future__ import unicode_literals

from django.db import models

class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 1:
            errors["first_name"] = "First name cannot be blank"
        if len(postData['last_name']) < 1:
            errors["last_name"] = "Last name cannot not be blank"
        if len(postData['email']) < 1:
            errors["email"] = "Email cannot not be blank"
        return errors
class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = BlogManager()
    



