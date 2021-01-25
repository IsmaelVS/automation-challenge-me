"""Base Page this project."""


class BasePage:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.home = self.driver.find_element_by_class_name(
            "logo.img-responsive"
        )
        self.search_field = self.driver.find_element_by_class_name(
            "search_query.form-control.ac_input"
        )
        self.search_button = self.driver.find_element_by_class_name(
            "btn.btn-default.button-search"
        )
        self.shopping_cart = self.driver.find_element_by_class_name(
            "ajax_cart_no_product"
        )

    def home_page(self) -> None:
        self.home.click()

    def access_cart(self) -> None:
        self.shopping_cart.click()

    def search(self, value: str) -> None:
        self.search_field.clear()
        self.search_field.send_keys(value)
        self.search_button.click()

    def contact(self) -> None:
        self.contact = self.driver.find_element_by_xpath(
            '//*[@id="contact-link"]'
        )
        self.contact.click()

    def menu(self) -> None:
        ...
