from flask import Blueprint, render_template, current_app #, session

from app.models.product import Product

product_routes = Blueprint("product_routes", __name__)

@product_routes.route("/products")
def products():
    products = Product.all()
    return render_template("products.html", products=products)
