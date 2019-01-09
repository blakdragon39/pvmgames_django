from __future__ import unicode_literals

from django.contrib.auth.models import User, PermissionsMixin
from django.db import models


User._meta.get_field('email')._unique = True
User._meta.get_field('first_name')._required = True
