import os
import sys


def build_env():
    import configurations

    configurations.setup()


def run():
    from configurations.management import execute_from_command_line

    build_env()
    execute_from_command_line(sys.argv)


def run_example():
    from django.core.management import execute_from_command_line

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example.settings")
    execute_from_command_line(sys.argv)


def wsgi():
    from configurations.wsgi import get_wsgi_application

    build_env()
    return get_wsgi_application()
