"""File to steps generics."""
from behave import given, step, then, when

from helpers.helper import select_item
from pages.base import BasePage


@given("que acesso o link")
def get(self):
    self.driver.get(
        "http://automationpractice.com/index.php?controller=authentication&back=my-account"
    )


@step("acesso a área de contato")
def to_contact(self):
    base = BasePage(self.driver)
    base.contact()


@when("preencho com os seguintes dados")
def message_contact(self):
    table = {row['Name']: row['Value'] for row in self.table}

    select_item(self, 'id_contact', table['subject'])

    email_field = self.driver.find_element_by_id("email")
    email_field.send_keys(table['email'])

    order_field = self.driver.find_element_by_id("id_order")
    order_field.send_keys(table['order'])

    message_field = self.driver.find_element_by_id("message")
    message_field.send_keys(table['message'])

    send = self.driver.find_element_by_xpath('//*[@id="submitMessage"]/span')
    send.click()


@then('a mensagem deve ser enviada com "{message}"')
def result(self, message: str):
    if message == "sucesso":
        alert = self.driver.find_element_by_class_name('alert.alert-success')

        assert alert.text == 'Your message has been successfully sent to our team.'
    else:
        alert = self.driver.find_element_by_class_name('alert.alert-danger')

        assert alert.text.split('\n')[-1] == 'The message cannot be blank.'
