
from flask import Blueprint, render_template, flash, redirect, current_app, url_for, session, request #, jsonify

from app.models.order import Order
from web_app.routes.wrappers import authenticated_route

order_routes = Blueprint("order_routes", __name__)

#
# USER ORDERS
#

@order_routes.route("/user/orders")
@authenticated_route
def orders():
    print("USER ORDERS...")
    current_user = session.get("current_user")
    orders = Order.where(user_email=current_user["email"])
    # sort descending on the basis of creation date:
    orders = sorted(orders, key=lambda order: order.created_at, reverse=True)
    return render_template("user_orders.html", orders=orders)


@order_routes.route("/user/orders/create", methods=["POST"])
@authenticated_route
def create_order():
    print("CREATE USER ORDER...")

    form_data = dict(request.form)
    print("FORM DATA:", form_data)
    product_id = form_data["product_id"]
    product_name = form_data["product_name"]
    product_price = form_data["product_price"]

    current_user = session.get("current_user")
    user_email = current_user["email"]

    try:
        params = {
            "user_email": user_email,
            "product_id": int(product_id),
            "product_name": product_name,
            "product_price": float(product_price)
        }
        #order = Order(params)
        #order.save()
        # alternatively:
        Order.create(params)

        flash(f"Order received!", "success")
        return redirect("/user/orders")
    except Exception as err:
        print(err)
        flash(f"Oops, something went wrong: {err}", "warning")
        return redirect("/products")
