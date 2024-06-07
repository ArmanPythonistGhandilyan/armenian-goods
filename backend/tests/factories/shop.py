import factory
from api.v1.apps.shops.models.shops import Shop
from factory.django import DjangoModelFactory, ImageField


class ShopModelFactory(DjangoModelFactory):
    class Meta:
        model = Shop

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    phone = factory.Faker("phone_number")
    shop_name = factory.Faker("company")
    shop_url = factory.Faker("url")
    logo = ImageField()
    banner = ImageField()
    street1 = factory.Faker("street_address")
    street2 = factory.Faker("secondary_address")
    city = factory.Faker("city")
    zip_code = factory.Faker("postcode")
    country = factory.Faker("country_code")
    state = factory.Faker("state")
    password = factory.Faker("password")
    confirm_password = password
    is_visible = factory.Faker("boolean")


# import factory
# from api.v1.apps.shops.models.shops import Shop
# from factory.django import DjangoModelFactory
# import pytest

# @pytest.mark.django_db
# class ShopModelFactory(DjangoModelFactory):
#


# shop = ShopFactory()
