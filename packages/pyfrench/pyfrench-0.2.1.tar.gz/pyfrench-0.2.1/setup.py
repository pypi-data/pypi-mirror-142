from setuptools import find_packages, setup

setup(
    name='pyfrench',
    packages=find_packages(),
    version='0.2.1',
    description='Une librairie qui traduit python en français',
    long_description='Une bibliothèque python de n\'importe quelle version qui traduit et ajoute la même fonctionnalité python au module.',
    author='Artic#6377',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'], 
    tests_require=['pytest'], 
    test_suite='tests',
    author_email="artic.admisoffi@gmail.com"
)