from setuptools import find_packages, setup

setup(
    name='pyfrench',
    packages=find_packages(),
    version='0.2.2b',
    description='Une librairie qui traduit python en français',
    long_description='Une bibliothèque python de n\'importe quelle version qui traduit et ajoute la même fonctionnalité python au module.',
    author='Artic#6377',
    license='MIT',
    url='https://github.com/ArticOff/pyfrench',
    install_requires=[],
    setup_requires=['pytest-runner'], 
    tests_require=['pytest'], 
    test_suite='tests',
    author_email="artic.admisoffi@gmail.com",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: French',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ]
)