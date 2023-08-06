from setuptools import setup

setup(
    name='tickstore-python-client',
    version='1.0',
    packages=['tickstore', 'tickstore/db', 'tickstore/query', 'tickstore/writers'],
    url='https://gitlab.com/alphaticks/tickstore-python-client',
    license='copyright',
    author='Alphatikcs',
    description='client to communicate with tickstore',
    install_requires=[
        'grpcio==1.37.1',
        'protobuf==3.16.0',
        'six==1.13.0',
        'tickstore-grpc==1.0',
    ]
)
