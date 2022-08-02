from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
import uuid
from ..managers import UserManager
from django.utils import timezone


class MovieUser(AbstractBaseUser, PermissionsMixin):
    # Hack to neglate this fields from the existing user model of Django
    username = models.CharField(blank=True, null=True, max_length=255)
    password = models.CharField(blank=True, null=True, max_length=255)

    UID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country_code = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, unique=True, blank=True, null=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # last_login and last_login (with this info we can send notifications to user who are login differently etc)
    last_login_time = models.DateTimeField(blank=True, null=True)
    last_logout_time = models.DateTimeField(blank=True, null=True)

    # date and time when this bizUser was created
    date_created = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["password", "is_staff"]

    objects = UserManager()

    def __str__(self):
        """Return a human readable representation of the MovieUser instance."""
        return "(UID: {}, PHONE: {}{})".format(
            self.UID, self.country_code, self.phone_number
        )

    class Meta:
        app_label = "api"
        unique_together = ["country_code", "phone_number"]


