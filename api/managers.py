from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_superuser(self, phone_number, password, is_staff, **extra_fields):
        if not phone_number or not password:
            raise ValueError("The given phone_number, password, is_staff must be set")

        user = self.model(phone_number=phone_number, is_staff=is_staff, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
