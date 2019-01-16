from __future__ import unicode_literals

from django.contrib.auth.models import User, PermissionsMixin


User._meta.get_field('email')._unique = True

