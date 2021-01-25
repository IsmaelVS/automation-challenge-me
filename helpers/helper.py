"""File for helper in project."""
from selenium.webdriver.support.ui import Select


def select_item(self, id, value):
    select_field = self.driver.find_element_by_id(id)
    select = Select(select_field)
    options = select.options

    for option in options:
        if option.text.strip() == value:
            option.click()
