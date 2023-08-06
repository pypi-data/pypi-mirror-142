import os
import os.path


def _find_recursive(name):
    parts = os.getcwd().split(os.sep)
    for x in range(len(parts), 0, -1):
        f = os.sep.join(parts[0:x] + [name])
        if os.path.isfile(f):
            return f
    raise FileNotFoundError


def _get_dot_env():
    from dotenv import dotenv_values

    try:
        return dotenv_values(_find_recursive(".env"))
    except FileNotFoundError:
        return {}


def _get_pyproject_toml():
    import toml

    return toml.load(_find_recursive("pyproject.toml"))
