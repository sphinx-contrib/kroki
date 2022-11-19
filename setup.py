from setuptools import find_namespace_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="sphinxcontrib-kroki",
    version="1.3.0",
    author="Martin Hasoň",
    author_email="martin.hason@gmail.com",
    description="Kroki integration into sphinx",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sphinx-contrib/kroki",
    packages=find_namespace_packages(include=["sphinxcontrib.*"]),
    classifiers=[
        "Framework :: Sphinx :: Extension",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "sphinx",
        "requests>=2.4.2",
        "pyyaml"
    ],
    extras_require={
        "code": ["black", "flake8", "mypy"],
        "test": [
            "coverage",
            "pytest",
            "pytest-cov",
        ],
        "extra": [
        ],
    },
)
