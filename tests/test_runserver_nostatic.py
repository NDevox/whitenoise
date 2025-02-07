from __future__ import unicode_literals

import django
from django.core.management import get_commands, load_command_class
import pytest


@pytest.fixture(autouse=True)
def setup():
    yield django.setup()


def get_command_instance(name):
    app_name = get_commands()[name]
    return load_command_class(app_name, name)


def test_command_output():
    command = get_command_instance("runserver")
    parser = command.create_parser("manage.py", "runserver")
    assert "Wrapped by 'whitenoise.runserver_nostatic'" in parser.format_help()
    assert not parser.get_default("use_static_handler")
