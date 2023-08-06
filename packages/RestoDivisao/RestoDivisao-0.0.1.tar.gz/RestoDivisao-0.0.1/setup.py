from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="RestoDivisao",
    version="0.0.1",
    author="lucio",
    author_email="ljsmonteiro@gmail.com",
    description="Resto da divisão",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ljsmonteiro/simple-package-template",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.5',
)