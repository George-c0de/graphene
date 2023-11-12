from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class Car(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    brand = models.CharField("Марка машины", max_length=100)
    model = models.CharField("Модель машины", max_length=100)
    plate_number = models.CharField("Номер машины", max_length=20, unique=True)
    owners_name = models.CharField("ФИО владельца", max_length=100)
    created_at = models.DateTimeField("Дата создания записи", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления записи", auto_now=True)

    def __str__(self):
        return f"{self.brand} - {self.model}"


class User(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField("Дата создания записи", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления записи", auto_now=True)

    def __str__(self):
        return f"{self.uuid}"

    class Meta:
        unique_together = ("uuid", "username")


User._meta.get_field("groups").remote_field.related_name = "custom_user_set"
User._meta.get_field(
    "user_permissions"
).remote_field.related_name = "custom_user_permissions"
