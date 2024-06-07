import os
import uuid
from io import BytesIO
from typing import override

from api.v1.apps.common.models import TimedBaseModel
from django.core.files import File
from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from PIL import Image


class Shop(TimedBaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField("First Name", max_length=20)
    last_name = models.CharField("Last Name", max_length=20)
    email = models.EmailField("Email", unique=True)
    phone = PhoneNumberField(
        "Phone Number",
        unique=True,
    )
    shop_name = models.CharField("Shop Name", max_length=50, unique=True)
    shop_url = models.URLField("Shop URL", unique=True)
    logo = models.ImageField("Logo", upload_to="logos/", blank=True, null=True)
    banner = models.ImageField(
        "Banner",
        upload_to="banners/",
        blank=True,
        null=True,
    )
    street1 = models.CharField("Street 1", max_length=50)
    street2 = models.CharField("Street 2", max_length=50, blank=True)
    city = models.CharField("Town / City", max_length=100)
    zip_code = models.CharField("Zip Code", max_length=10)
    country = CountryField("Country", blank_label="(select country)")
    state = models.CharField("State", max_length=100, blank=True, default="")
    password = models.CharField("Password")
    confirm_password = models.CharField("Confirm Password")
    is_visible = models.BooleanField(
        verbose_name="Is the shop visible in the shops catalog",
        default=True,
    )

    class Meta:
        verbose_name = "Խանութ"
        verbose_name_plural = "Խանութներ"
        app_label = "shops"

    def __str__(self):
        return self.shop_name

    @override
    def save(self, *args, **kwargs):
        if self.logo:
            super().save(*args, **kwargs)

            logo_path = self.logo.path

            logo = Image.open(logo_path)
            logo_size = os.path.getsize(logo_path)  # in bytes
            thirty_mb = 30 * 1024 * 1024

            while logo_size > thirty_mb:
                logo = logo.convert("RGB")
                logo.save(
                    logo_path,
                    quality=60,
                    optimize=True,
                    format="JPEG",
                )
                logo_size = os.path.getsize(logo_path)

            self.logo = logo
        else:
            super().save(*args, **kwargs)
