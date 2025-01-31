"""Hooks to the project."""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as opt_chrome
from selenium.webdriver.firefox.options import Options as opt_firefox

from ipdb import post_mortem


def before_step(context, step) -> None:
    """Performs before all steps."""

    ...


def before_scenario(context, scenario) -> None:
    """Performs before all scenarios."""

    ...


def before_feature(context, feature) -> None:
    """Performs before all feature."""

    ...


def before_tag(context, tag) -> None:
    """Performs before all tag."""

    ...


def before_all(context) -> None:
    """Performs before all."""

    context.userdata = context.config.userdata
    context.debug = context.userdata["debug"]
    context.browser = context.userdata["browser"].lower()
    context.background = context.userdata["background"]

    desired_cap = {"browserName": context.browser}

    options = opt_firefox() if context.browser == "firefox" else opt_chrome()

    options.add_argument("--start-maximized")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")

    if context.background == 'True':
        context.driver = webdriver.Remote(
            options=options, desired_capabilities=desired_cap
        )
    else:
        context.driver = webdriver.Remote(
            desired_capabilities=desired_cap
        )


def after_step(context, step) -> None:
    """Performs after step."""

    if context.debug == "True" and step.status == "failed":
        post_mortem(step.exc_traceback)

    if step.status == "failed":
        context.driver.save_screenshot('./reports/error.png')


def after_scenario(context, scenario) -> None:
    """Performs after all scenarios."""

    ...


def after_feature(context, feature) -> None:
    """Performs after all feature."""

    ...


def after_tag(context, tag) -> None:
    """Performs after all tag."""

    ...


def after_all(context) -> None:
    """Performs after all."""

    context.driver.close()
