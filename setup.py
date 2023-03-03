from setuptools import setup, find_packages

def read_requirements(file):
    with open(file) as f:
        return f.read().splitlines()

def read_file(file):
   with open(file) as f:
        return f.read()
    
long_description = read_file("README.")
version = read_file("VERSION")
requirements = read_requirements("requirements.txt")

setup(
    name = 'mexcpy',
    version = version,
    author = 'PurpRabbit',
    url = 'https://best-practice-and-impact.github.io/example-package-python/',
    description = 'Python3 Mexc Api wrapper',
    long_description_content_type = "text/markdown",
    long_description = long_description,
    license = "MIT license",
    install_requires = requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]  
)