"""File to steps register."""
from time import sleep

from behave import given, step, then

from helpers.helper import select_item
from pages.register import Register


@when('preencho com o seguinte email "{email}"')
def validate_email(self, email):
    register = Register(self.driver)
    register.validate_email(email)
    sleep(2)


@then('deve ser preenchido com os seguintes dados')
def register_user(self):
    table = {row['Name']: row['Value'] for row in self.table}

    radio = self.driver.find_elements_by_class_name('radio-inline')

    for r in radio:
        if r.text == table['title']:
            r.click()

    first_name = self.driver.find_element_by_id('customer_firstname')
    first_name.send_keys(table['first name'])

    last_name = self.driver.find_element_by_id('customer_lastname')
    last_name.send_keys(table['last name'])

    password = self.driver.find_element_by_id('passwd')
    password.send_keys(table['password'])

    select_item(self, 'days', table['day'])

    select_item(self, 'months', table['month'])

    select_item(self, 'years', table['year'])

    newsletter = self.driver.find_element_by_id('newsletter')
    if table['newletter'] == 'True':
        newsletter.click()

    partners = self.driver.find_element_by_id('optin')
    if table['partners'] == 'True':
        partners.click()

    company = self.driver.find_element_by_id('company')
    company.send_keys(table['company'])

    address1 = self.driver.find_element_by_id('address1')
    address1.send_keys(table['address1'])

    address2 = self.driver.find_element_by_id('address2')
    address2.send_keys(table['address2'])

    city = self.driver.find_element_by_id('city')
    city.send_keys(table['city'])

    select_item(self, 'id_state', table['state'])

    postcode = self.driver.find_element_by_id('postcode')
    postcode.send_keys(table['post code'])

    select_item(self, 'id_country', table['country'])

    other = self.driver.find_element_by_id('other')
    other.send_keys(table['other'])

    phone = self.driver.find_element_by_id('phone')
    phone.send_keys(table['phone'])

    phone_mobile = self.driver.find_element_by_id('phone_mobile')
    phone_mobile.send_keys(table['phone_mobile'])

    alias = self.driver.find_element_by_id('alias')
    alias.send_keys(table['alias'])

    register = self.driver.find_element_by_id('submitAccount')
    register.click()


@step('deve ser cadastrado')
def validate_register(self):
    message = self.driver.find_element_by_class_name('page-heading')

    assert message.text == 'MY ACCOUNT'


@then('deve exibir a mensagem de erro')
def email_invalid(self):
    message = self.driver.find_elements_by_class_name('alert.alert-danger')

    assert message
