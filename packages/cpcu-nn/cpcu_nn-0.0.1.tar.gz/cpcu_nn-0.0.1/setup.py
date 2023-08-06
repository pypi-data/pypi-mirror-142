from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'cpcu love love'
LONG_DESCRIPTION = 'cpcu with love'

setup(
    name="cpcu_nn",
    version=VERSION,
    author="phoompat",
    author_email="phoompat@phoompat.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    package_dir={"": "src"},
    packages=find_packages(where='src'),
    project_url="https://github.com/peem5210/cpcu_nn",
    keywords=['phoompat'],
    classifiers=[
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
    ]
)
