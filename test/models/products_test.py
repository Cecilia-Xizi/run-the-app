
from datetime import datetime

from app.models.product import Product

from conftest import GOOGLE_SHEETS_TEST_DOCUMENT_ID

def test_products(model_context):
    # model context ensures tests are using data from the test document:
    assert Product.service.document_id == GOOGLE_SHEETS_TEST_DOCUMENT_ID

    # DESTROY ALL:

    Product.destroy_all()

    # SEED RECORDS:

    Product.seed()

    # FIND ALL:

    products = Product.all()
    assert len(products) == 3

    # CREATE

    product = Product.find(1)
    assert product.id == 1
    assert product.name == "Strawberries"
    assert product.price == 4.99
    assert isinstance(product.created_at, datetime)
