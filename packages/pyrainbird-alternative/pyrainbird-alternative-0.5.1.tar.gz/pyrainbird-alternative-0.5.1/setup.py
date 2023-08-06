import shlex
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [("pytest-args=", "a", "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ""

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)


setup(
    name="pyrainbird-alternative",
    version="0.5.1",
    description="Rain Bird Controller",
    install_requires=['pycryptodome', 'requests~=2.27.0', 'datetime~=4.3', 'setuptools~=56.0.0', 'PyYAML~=5.1.2'],
    tests_require=['responses', 'parameterized', 'mccabe', 'pyflakes', 'pytest-cov', 'pytest-flakes', 'pytest-mccabe',
                   'pytest-pep8', 'pytest-mock', 'pytest', 'six', 'requests', 'setuptools'],
    # The project's main homepage.
    url="https://github.com/konikvranik/pyrainbird/",
    # Author details
    author="konikvranik",
    author_email="hpa@suteren.net",
    license="MIT",
    keywords=["Rain Bird"],
    classifiers=[],
    zip_safe=True,
    cmdclass={"test": PyTest},
    packages=find_packages(exclude=("test", "test.*")),
    package_data={'': ['sipcommands.yaml', 'models.yaml', 'requirements.txt']},
    include_package_data=True,
)
