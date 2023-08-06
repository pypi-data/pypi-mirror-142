from setuptools import setup
from codecs import open
from os import path

HERE = path.abspath(path.dirname(__file__))
with open(path.join(HERE, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="quickerml",
    version="0.1.0",
    description="Machine learning toolkit to find the best starting model for your project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://quickerml.readthedocs.io/",
    author="Rafael Moret",
    author_email="rafaelmoretgalan@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    packages=["quickerml"],
    include_package_data=True,
    install_requires=[
        "pandas",
        "numpy",
        "tqdm",
        "catboost",
        "lightgbm",
        "xgboost",
        "scikit-learn",
    ],
)
