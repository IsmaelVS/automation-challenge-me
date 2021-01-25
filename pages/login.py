"""Base Page login."""


class Login:
    def __init__(self, driver):
        self._driver = driver
        self._email_field = self._driver.find_element_by_id("email")
        self._passwd_field = self._driver.find_element_by_id("passwd")
        self._sign_in = self._driver.find_element_by_id("SubmitLogin")

    def login(self, email: str, passwd: str) -> None:
        self._email_field.clear()
        self._email_field.send_keys(email)
        self._passwd_field.clear()
        self._passwd_field.send_keys(passwd)
        self._sign_in.click()
