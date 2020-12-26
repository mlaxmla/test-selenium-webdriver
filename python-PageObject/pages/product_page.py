from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        # self.wait = WebDriverWait(driver, 10)


def add_one_product(app):
    # 1) otwórz stronę jakiegoś towaru,
    app.driver.find_element(By.XPATH, "//*[@id='box-most-popular']//a[@class='link'][@title!='Yellow Duck']").click()
    # 2) dodaj go do koszyka,
    app.wait.until(EC.presence_of_element_located((By.NAME, "add_cart_product")))
    cart_quantity_before = int(app.driver.find_element(By.XPATH, "//*[@id='cart']//span[@class='quantity']").text)
    app.driver.find_element_by_name("add_cart_product").click()
    # 3) poczekaj, aż licznik towarów w koszyku odświeży się,
    # todo: I would like to wait until script ends, but it doesn't work :( Please explain how to wait until finish of function updateCart() from http://localhost/litecart/ext/jquery/jquery-1.12.4.min.js? I've found an example with execute_script in LMS but I don't know how to debug methods/arguments of scripts used in application under test??
    # wait.until(lambda driver: wd.execute_script("return jQuery.active == 0")) # return window.jQuery!=undefined && jQuery.active==0
    # HINT: You also have to:
    # 1) After adding an item to the cart, wait until the number of items increases by one
    app.wait.until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='cart']//span[@class='quantity'][.='" + str(cart_quantity_before + 1) + "']")))
    # time.sleep(2)
    # 4) wróć na stronę główną i powtórz poprzednie kroki jeszcze dwa razy, aby w sumie w koszyku były trzy sztuki towaru,
    # wd.get("http://localhost/litecart/")
    # CustomerLandingPage.open(app)
    app.driver.find_element_by_link_text("Home").click()


def remove_all_products(app):
    # 5) otwórz koszyk (kliknij na link Checkout w prawem górnym rogu),
    app.driver.find_element_by_link_text("Checkout »").click()
    app.wait.until(EC.presence_of_element_located((By.NAME, "remove_cart_item")))
    order_summary_len = len(
        app.driver.find_elements(By.XPATH, "//*[@id='order_confirmation-wrapper']/table/tbody/tr/td[@class='item']"))
    # 6) usuń wszystkie towary z koszyka, jeden za drugim. Po każdym usunięciu poczekaj, aż odświeży się tabela na dole.
    for j in range(order_summary_len):
        order_summary_before_len = len(
            app.driver.find_elements(By.XPATH,
                                     "//*[@id='order_confirmation-wrapper']/table/tbody/tr/td[@class='item']"))
        # HINT 2+: In addition, the page has a "carousel" that displays the contents of the cart, products are displayed and hidden, this may affect the ability to click the delete button. To stop the carousel, you can first click on the small product icon below it, then this product will open and you can safely press the delete button, it will not hide.
        if app.driver.find_element(By.XPATH, "//*[@id='box-checkout-cart']//li/a"):
            app.driver.find_element(By.XPATH, "//*[@id='box-checkout-cart']//li/a").click()

        app.driver.find_element(By.NAME, "remove_cart_item").click()  # .submit()
        # todo: how to wait for table refresh and how to detect precisely a state of the last element erasure? Is there better way to do this without counting table rows before and after each remove action??
        # wait.until(lambda d: d.find_element_by_name("remove_cart_item"))
        # HINT: You also have to:
        # 2) After clicking on the button to delete an item, wait for the table to update.
        app.wait.until_not(EC.presence_of_element_located((By.XPATH,
                                                           "(//*[@id='order_confirmation-wrapper']/table/tbody/tr/td[@class='item'])[" + str(
                                                               order_summary_before_len) + "']")))