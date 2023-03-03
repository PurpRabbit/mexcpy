from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mexcpy",
    version="1.0.1",
    author="PurpRabbit",
    author_email="lysovich28@gmail.com",
    description="Python3 Mexc API wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PurpRabbit/mexcpy",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    install_requires=[
        'requests==2.28.2',
    ],
)
