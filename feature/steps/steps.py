from behave import given


@given("que acesso o link")
def get(self):
    self.driver.get(
        "http://automationpractice.com/index.php?controller=authentication&back=my-account"
    )
