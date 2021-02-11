from django.db.models import *
from django.utils.crypto import get_random_string


# Create your models here.

# Token auth
class Token(Model):
    token = CharField(max_length=50, default=get_random_string(50))
    code = CharField(max_length=6, default=get_random_string(allowed_chars='123456789'))
    email = CharField(max_length=200)


# Classes Model
class Classes(Model):
    name = CharField(max_length=100)
    Image = FileField(upload_to='classes/', verbose_name=get_random_string(50))

    def __str__(self):
        return self.Image.url


# Teacher Users
class Admin(Model):
    # Admin Info
    token = CharField(max_length=30, default=get_random_string(length=30), unique=True)
    id = CharField(max_length=50, unique=True, primary_key=True)
    password = CharField(max_length=50)
    email = CharField(max_length=500)
    name = CharField(max_length=100)
    profilePicture = FileField(upload_to='Admins', verbose_name=get_random_string(50), blank=True,)
    # Admin Related
    classes = ManyToManyField(Classes, blank=True)

    # def
    def __str__(self):
        return self.profilePicture.url
