from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="sphinx-kroki",
    version="1.0.0",
    author="Martin Hasoň",
    author_email="martin.hason@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hason/sphinx-kroki",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "sphinx",
        "requests>=2.4.2",
    ],
    extras_require={
        "code": ["black", "mypy"],
        "testing": [
            "coverage",
            "pytest",
            "pytest-cov",
        ],
    },
)
