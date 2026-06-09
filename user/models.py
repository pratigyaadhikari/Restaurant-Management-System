from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=15, unique=True)
    USERNAME_FIELD = "phone"






# paila hamro: default username
#              admin    theyo

# User model
# admin

# but after changing user(AbstractUser), ahela ko flow
# admin paxi balla 
# user model aako xa

# default user
# admin
# User model

# so dependency error dekhairaxa, eslai solve garna we have to create a different database