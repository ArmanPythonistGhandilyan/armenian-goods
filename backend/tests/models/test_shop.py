"""
Comments here
"""

from api.v1.apps.shops.models.shops import Shop
import pytest

from ..factories.shop import ShopModelFactory



@pytest.mark.django_db(transaction=True)
def test_shop_creation():
    shop = ShopModelFactory()
    assert Shop.objects.count() == 1
    assert Shop.objects.first() == shop
    assert shop.first_name
    assert shop.last_name
    assert shop.email
    assert shop.phone
    assert shop.shop_name
    assert shop.shop_url
    assert shop.street1
    assert shop.city
    assert shop.zip_code
    assert shop.country
    assert shop.state
    assert shop.password
    assert shop.confirm_password
    assert isinstance(shop.is_visible, bool)

@pytest.mark.django_db
def test_simple_test():
    """
    Comments here
    """
    a = 28

    assert a == 28, f"{a=}" # if fail will show "a=38"