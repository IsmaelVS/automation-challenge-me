"""File to steps login."""
from time import sleep

from behave import given, step, then

from pages.login import Login


@step('realizo o login com os campos "{email}" e "{senha}"')
def _(self, email: str, senha: str):
    login_page = Login(self.driver)
    login_page.login(email, senha)


@step('realizo o login com os campos "" e ""')
def _(self):
    login_page = Login(self.driver)
    login_page.login("", "")


@then('o login deve ser finalizado com "{message}"')
def result(self, message: str):
    if message == "sucesso":
        center_column = self.driver.find_element_by_id("center_column")
        info_account = center_column.find_element_by_class_name("info-account")

        assert "Welcome" in info_account.text
    else:
        error = self.driver.find_element_by_class_name("alert.alert-danger")

        assert message in error.text


@step("devo deslogar")
def logout(self):
    self.driver.find_element_by_class_name("logout").click()
