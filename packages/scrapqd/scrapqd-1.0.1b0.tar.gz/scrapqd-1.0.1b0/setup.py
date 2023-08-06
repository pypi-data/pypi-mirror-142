import sys
from os import path

import setuptools
from setuptools.command.test import test as TestCommand  # noqa

import scrapqd

DIR = path.abspath(path.dirname(__file__))

with open("README.rst") as f:
    readme = f.read()


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)


setuptools.setup(
    name="scrapqd",
    packages=setuptools.find_packages(exclude=("tests",)),
    version=scrapqd.__version__,
    author=scrapqd.__author__,
    author_email=scrapqd.__contact__,
    description=scrapqd.__description__,
    long_description=readme,
    long_description_content_type="text/x-rst",
    url="https://github.com/dduraipandian/scapqd",
    package_dir={"scrapqd": "scrapqd"},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    keywords=scrapqd.__keywords__,
    python_requires=">=3.7",
    tests_require=["tox"],
    cmdclass={"test": Tox},
    zip_safe=False,
    include_package_data=True,
    package_data={
        "": [
            "settings/user_agents.dat",
            "gql/template.html",
            "_static/sample.html"
        ]
    },
    install_requires=[
        "lxml==4.8.0",
        "flask==2.0.3",
        "graphql-server==3.0.0b5",
        "requests==2.27.1",
        "graphql-core==3.2.0",
        "selenium==4.1.3",
        "immutable-config==1.0",
        "webdriver-manager==3.5.3"
    ],
)
