import os

from setuptools import find_packages, setup


def get_version():
    basedir = os.path.dirname(__file__)
    with open(os.path.join(basedir, "src/sonantic/version.py")) as f:
        locals = {}
        exec(f.read(), locals)
        return locals["__version__"]


def get_long_description():
    with open("README.md", encoding="utf8") as f:
        return f.read()


extras = {}
extras["dev"] = ["black", "isort", "pre-commit", "build", "twine"]
extras["test"] = ["pytest"]
install_requires = ["requests", "pydantic"]
extras["all"] = install_requires + extras["test"] + extras["dev"]

setup(
    name="sonantic",
    description="Python client for the Sonantic API",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/sonantic-samples/sonantic-python",
    license="MIT",
    author="Sonantic",
    author_email="support@sonantic.io",
    package_dir={"": "src"},
    packages=find_packages("src"),
    version=get_version(),
    python_requires=">=3.8",
    zip_safe=False,
    install_requires=install_requires,
    include_package_data=True,
    tests_require=["pytest"],
    extras_require=extras,
    package_data={
        "sonantic": [
            "py.typed",
        ]
    },
)
