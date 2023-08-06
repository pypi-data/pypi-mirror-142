import os
import re
import subprocess
from enum import Enum

import typer
from plumbum import FG, ProcessExecutionError
from plumbum import local as lr

from tuhls.gosu import _get_pyproject_toml

app = typer.Typer()


def git(*args, output=True):
    r = subprocess.check_output(["git"] + list(args))
    if output:
        print(args)  # noqa
        print(r)  # noqa
    return r


def git_num_changes():
    return len(git("status", "--porcelain").splitlines())


def _get_version():
    return git("describe", "--tags").decode().strip()


@app.command()
def push_repo():
    git(
        "remote",
        "set-url",
        "--push",
        "origin",
        re.sub(r".+@([^/]+)/", r"git@\1:", os.environ["CI_REPOSITORY_URL"]),
    )
    git("push", "-o", "ci.skip", "origin", get_version())


class SemverPart(str, Enum):
    patch = "patch"
    minor = "minor"
    major = "major"


@app.command()
def bump_version(semver_part: SemverPart = SemverPart.patch):
    import semver
    import toml

    git("fetch", "--tags", "-f")
    git("tag")
    try:
        v = _get_version()
        if semver_part.value == SemverPart.patch:
            n = semver.bump_patch(v)
        elif semver_part.value == SemverPart.minor:
            n = semver.bump_minor(v)
        elif semver_part.value == SemverPart.major:
            n = semver.bump_major(v)
    except (subprocess.CalledProcessError, ValueError):
        print("initialise versioning with 1.0.0")  # noqa
        git("tag", "1.0.0")
        return

    if "-" not in v:
        return

    print(f"bump from {v} to {n}")  # noqa
    data = _get_pyproject_toml()
    data["project"]["version"] = n
    with open("pyproject.toml", "w") as f:
        toml.dump(data, f)
    git("add", ".")
    git("commit", "--allow-empty", "-m", f"bump version to {n}")
    git("push", "-o", "ci.skip")
    git("tag", "-a", n, "-m", f"release {n}")
    git("push", "--follow-tags")


@app.command()
def get_version():
    print(f"current version: {_get_version()}")  # noqa


@app.command()
def local():
    has_changes = git_num_changes() > 0
    try:
        if has_changes:
            git("add", ".")
            git("commit", "-m", "local debug commit")
        (
            lr["gitlab-ci-local"][
                "--privileged",
            ]
            & FG
        )
    except ProcessExecutionError:
        exit(1)
    finally:
        if has_changes:
            git("reset", "HEAD~1")


def get_project_name():
    return _get_pyproject_toml()["project"]["name"]


def get_project_version():
    return _get_pyproject_toml()["project"]["version"]


def get_name_version():
    return f"{get_project_name()}:{get_project_version()}"


@app.command()
def docker():
    lr["cp"]["Dockerfile", "dist/Dockerfile"] & FG
    lr.cwd.chdir("dist")
    (
        lr["docker"][
            "build",
            "--no-cache",
            "-t",
            get_project_name(),
            "-t",
            get_name_version(),
            ".",
        ]
        & FG
    )


@app.command()
def podman_login():
    (
        lr["podman"][
            "login",
            "-u",
            os.environ["CI_REGISTRY_USER"],
            "-p",
            os.environ["CI_REGISTRY_PASSWORD"],
            os.environ["CI_REGISTRY"],
        ]
        & FG
    )


@app.command()
def podman_build():
    lr["cp"]["Dockerfile", "dist/Dockerfile"] & FG
    lr.cwd.chdir("dist")
    registry_name = os.environ["CI_REGISTRY_IMAGE"]
    (
        lr["podman"][
            "build",
            "-t",
            f"{registry_name}/{get_project_name()}",
            "-t",
            f"{registry_name}/{get_name_version()}",
            ".",
        ]
        & FG
    )


@app.command()
def podman_push():
    registry_name = os.environ["CI_REGISTRY_IMAGE"]
    lr["podman"]["push", f"{registry_name}/{get_project_name()}"] & FG
    lr["podman"]["push", f"{registry_name}/{get_name_version()}"] & FG


@app.command()
def twine_gitlab_upload():
    if "CI_COMMIT_TAG" not in lr.env:
        return
    lr.env["TWINE_PASSWORD"] = lr.env["CI_JOB_TOKEN"]
    lr.env["TWINE_USERNAME"] = "gitlab-ci-token"
    (
        lr["python"][
            "-m",
            "twine",
            "upload",
            "--repository-url",
            f'{lr.env["CI_API_V4_URL"]}/projects/{lr.env["CI_PROJECT_ID"]}/packages/pypi',
            "dist/*",
        ]
        & FG
    )


@app.command()
def twine_pypi_upload():
    if "CI_COMMIT_TAG" not in lr.env:
        return
    lr.env["TWINE_PASSWORD"] = lr.env["PYPI_TOKEN"]
    lr.env["TWINE_USERNAME"] = "__token__"
    (
        lr["python"][
            "-m",
            "twine",
            "upload",
            "--repository-url",
            "https://upload.pypi.org/legacy/",
            "dist/*",
        ]
        & FG
    )
