from __future__ import unicode_literals
from django.db import models
import bcrypt, datetime

class UserManager(models.Manager):
    def login(self, user):
        query_user = User.objects.filter(email=user.get('email_login')).first()
        if query_user and bcrypt.hashpw(user['password_login'].encode(), query_user.password.encode()) == query_user.password:
                return True

        return False

    def registration(self, user):
        validation = True
        if len(user['first_name']) < 3:
            validation = False
        if len(user['last_name']) < 3:
            validation = False
        if len(user['email']) < 8:
            validation = False
        if len(user['password']) < 8:
            validation = False
        if user.get('password') != user.get('password_confirm'):
            validation = False
        return validation


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    date_hired = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Wish(models.Model):
    product = models.CharField(max_length=50)
    user_creator = models.ForeignKey(User, related_name="creator")
    user_added = models.ManyToManyField(User, related_name="added")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
