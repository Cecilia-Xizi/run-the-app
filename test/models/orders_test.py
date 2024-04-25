
from app.models.order import Order

from conftest import GOOGLE_SHEETS_TEST_DOCUMENT_ID

def test_orders(model_context):
    # model context ensures tests are using data from the test document:
    assert Order.service.document_id == GOOGLE_SHEETS_TEST_DOCUMENT_ID

    # setup (no orders):
    Order.destroy_all()

    # create order:
    params = {
        "user_email": "example@gmail.com",
        "product_id": 999,
        "product_name": "Ninety Nine Bottles",
        "product_price": 9.99,
    }
    Order.create(params)

    # it should persist data to the sheet (so we can fetch it later)
    orders = Order.all()
    assert len(orders) == 1

    order = orders[0]
    assert order.user_email == "example@gmail.com"
    assert order.product_id == 999
    assert order.product_name == "Ninety Nine Bottles"
    assert order.product_price == 9.99
