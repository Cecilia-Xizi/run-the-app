
from flask import Blueprint, render_template, flash, redirect, current_app, url_for, session, request #, jsonify

from app.models.my_event import Event
from web_app.routes.wrappers import authenticated_route

my_event_routes = Blueprint("my_events_routes", __name__)

#
# USER ORDERS
#

@my_event_routes.route("user/my_events")
@authenticated_route
def my_events():
    print("USER EVENTS...")
    current_user = session.get("current_user")
    my_events = Event.where(user_email=current_user["email"])
    # sort descending on the basis of creation date:
    my_events = sorted(my_events, key=lambda order: my_event.created_at, reverse=True)
    return render_template("my_events.html", orders=my_events)


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