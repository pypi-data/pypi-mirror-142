from setuptools import find_packages, setup

VERSION = '0.1.0'

setup(
    name='pyloopkey',
    packages=find_packages(include=['loopkey_client']),
    version=VERSION,
    description='Loopkey API library',
    author='Mauricio Cisneros',
    author_email='mauricio.cisneros@casai.com',
    url='https://github.com/casai-org/pyloopkey',
    install_requires=['requests==2.26.0'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
