from setuptools import setup, find_packages

setup(
    name="vuln_app",
    version="1.0.0",
    description="Test package that has vulnerable dependency",
    install_requires=[
        "jinja2==2.11.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
)
