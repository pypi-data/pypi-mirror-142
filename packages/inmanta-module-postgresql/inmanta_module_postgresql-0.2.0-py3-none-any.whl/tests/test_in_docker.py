import os
import subprocess
import sys

import pytest


@pytest.fixture
def pip_lock_file() -> None:
    """get all versions of inmanta packages into a freeze file, to make the environment inside docker like the one outside"""
    with open("requirements.freeze.all", "w") as ff:
        subprocess.check_call([sys.executable, "-m", "pip", "freeze"], stdout=ff)
    with open("requirements.freeze.tmp", "w") as ff:
        subprocess.check_call(["grep", "inmanta", "requirements.freeze.all"], stdout=ff)
    # pip freeze can produce lines with @ that refer to folders outside the container
    # see also https://github.com/pypa/pip/issues/8174
    # also ignore inmanta-dev-dependencies as this is pinned in the requirements.dev.txt
    with open("requirements.freeze", "w") as ff:
        subprocess.check_call(
            [
                "grep",
                "-v",
                "-e",
                "@",
                "-e",
                "inmanta-dev-dependencies",
                "requirements.freeze.tmp",
            ],
            stdout=ff,
        )
    yield


@pytest.mark.skipif(
    not os.getenv("INMANTA_TEST_INFRA_SETUP", "false").lower() == "true",
    reason="Only run when test infra environment variable is set to true",
)
def test_docker(pip_lock_file, docker_container):
    print(f"Running tests in container {docker_container}")
    subprocess.run(
        [
            "sudo",
            "docker",
            "exec",
            f"{docker_container}",
            "env/bin/pytest",
            "tests/",
            "-v",
            "-s",
            "--log-cli-level",
            "DEBUG",
            "--junitxml=junit.xml",
        ],
        check=True,
    )
