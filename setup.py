from setuptools import setup, find_packages

setup(
    packages = find_packages(),
    package_data = {'': ['*.jpg', '*.ttf']},
    install_requires=[
    'fpdf',
    ]
)
