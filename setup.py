from setuptools import setup

setup(
    name='axisio',
    version='0.1.0',
    description='Library for controlling Axis camera IOs',
    author='Ahmed Radwan',
    author_email='ahmed.ali.radwan94@gmail.com',
    url='https://github.com/AhmedARadwan/axis-io',
    packages=['axisio'],
    install_requires=[
        'requests',
    ],
)