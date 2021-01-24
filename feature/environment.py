"""Hooks to the project."""


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

    ...


def after_step(context, step) -> None:
    """Performs after step."""

    ...


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

    ...
