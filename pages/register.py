from selenium.webdriver.support.ui import Select


class Register:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.email_register = self.driver.find_element_by_id(
            "email_create"
        )
        self.create = self.driver.find_element_by_id(
            "SubmitCreate"
        )

    def validate_email(self, email) -> None:
        self.email_register.send_keys(email)

        self.create.click()
