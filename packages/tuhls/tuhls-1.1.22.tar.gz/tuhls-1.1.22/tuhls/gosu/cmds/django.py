import glob
import os

import typer
from plumbum import FG, local

from tuhls.gosu import _get_dot_env, _get_pyproject_toml

app = typer.Typer()


def _manage_env_vars():
    env_vars = _get_dot_env()
    for name, value in env_vars.items():
        local.env[name] = value

    return env_vars


def _run(*cmds):
    _manage_env_vars()
    print(cmds)  # noqa
    local[cmds[0]][cmds[1:]] & FG


def _get_django_app_src():
    try:
        return _get_pyproject_toml()["gosu"]["django_app_src"]
    except Exception:
        return "example"


def _pm(*cmds):
    local.cwd.chdir(_get_django_app_src())
    _run("python", "manage.py", *cmds)
    local.cwd.chdir("..")


@app.command(
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True}
)
def pm(ctx: typer.Context):
    _pm(*ctx.args)


@app.command()
def migrate():
    _pm("makemigrations")
    _pm("migrate")


@app.command()
def gunicorn():
    _pm("collectstatic", "--no-input")
    _pm("migrate")
    local.cwd.chdir(_get_django_app_src())
    _run(
        "gunicorn",
        "--bind",
        "0.0.0.0:8000",
        "--workers=2",
        "--worker-tmp-dir",
        "/dev/shm",
        "base.wsgi:application",
    )


@app.command()
def test():
    _manage_env_vars()
    local.env["DEFAULT_CACHE"] = "locmemcache://"
    local.env["QUEUE_CACHE"] = "locmemcache://"
    rcfile = f"--rcfile={os.path.dirname(__file__)}/../.coveragerc"
    _run(
        "coverage",
        "run",
        "--concurrency=multiprocessing",
        "--parallel-mode",
        rcfile,
        f"{_get_django_app_src()}/manage.py",
        "test",
        "--parallel=3",
        ".",
    )
    _run("coverage", "combine", rcfile)
    _run("coverage", "report", "-i", rcfile)


@app.command()
def precommit():
    fix()
    test()
    build()


@app.command()
def notebook():
    local.env["DJANGO_ALLOW_ASYNC_UNSAFE"] = True
    _pm("shell_plus", "--notebook")


@app.command(
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True}
)
def run(ctx: typer.Context):
    _run(*ctx.args)


def _get_pkg_pyfiles():
    files = list(
        filter(
            lambda e: all(
                [not (x in e) for x in ["node_modules", "migrations", "build"]]
            ),
            glob.glob("**/*.py", recursive=True),
        )
    )
    print(files)  # noqa
    return files


@app.command()
def fix():
    _run("pyupgrade", "--py39-plus", "--exit-zero-even-if-changed", *_get_pkg_pyfiles())
    _run("isort", "--profile", "black", *_get_pkg_pyfiles())
    _run("black", *_get_pkg_pyfiles())
    _run("flake8", "--config", f"{os.path.dirname(__file__)}/../.flake8")


@app.command()
def lint():
    _run("pyupgrade", "--py39-plus", *_get_pkg_pyfiles())
    _run("isort", "--profile", "black", "-c", *_get_pkg_pyfiles())
    _run("black", "--check", *_get_pkg_pyfiles())
    _run("flake8", "--config", f"{os.path.dirname(__file__)}/../.flake8")


@app.command()
def build():
    _run("flit", "build")
