from pages.customer_landing_page import CustomerLandingPage
from pages.product_page import add_one_product, remove_all_products


def test_user_add_remove_products(app):
    CustomerLandingPage.open(app)
    # powtórz dodawanie produktu 3x
    for i in range(3):
        add_one_product(app)
    remove_all_products(app)
