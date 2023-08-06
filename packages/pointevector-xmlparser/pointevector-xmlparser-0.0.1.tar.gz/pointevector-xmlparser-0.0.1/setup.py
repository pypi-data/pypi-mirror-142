from setuptools import setup, find_namespace_packages

setup(
    name='pointevector-xmlparser',
    version='0.0.1',
    author='Andrew Hoekstra',
    author_email='andrew@pointevector.com',
    url='https://github.com/Pointe-Vector/xml_parser',
    packages=find_namespace_packages(include=['pointevector.*']),
    install_requires=[
        'typing_extensions',
    ],
)
