import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

setup(
    name='django-admin-autocomplete-filter',
    version='0.5',
    packages=find_packages(),
    include_package_data=True,
    description='A simple Django app to render list filters in django admin using autocomplete widget',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/farhan0581/django-admin-autocomplete-filter',
    author='Farhan Khan',
    author_email='farhan0581@gmail.com',
    install_requires=[
        'django>=2.0',
    ],
    classifiers=[
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
