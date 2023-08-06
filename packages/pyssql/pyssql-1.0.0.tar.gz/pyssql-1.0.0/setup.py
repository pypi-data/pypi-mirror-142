from setuptools import setup


def readme():
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()


setup(
    name="pyssql",
    version="1.0.0",
    description="An sql module that requires no knowledge of sql syntax.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Matthias1590/SimpleSql",
    author="Matthias Wijnsma",
    author_email="matthiasx95@gmail.com",
    license="MIT",
    python_requires=">=3.6",
    packages=["pyssql"],
)
