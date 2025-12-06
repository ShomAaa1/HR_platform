from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    class Roles(models.TextChoices):
        CANDIDATE = "candidate", "Candidate"
        HR = "hr", "HR Manager"
        ADMIN = "admin", "Administrator"

    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.CANDIDATE
    )

    # исправляем конфликты reverse accessor
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # <-- меняем related_name
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",  # <-- меняем related_name
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
