import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-admin-multiple-choice-list-filter',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD 2-Clause "Simplified" License',
    description='A Django app to add a Multiple Choice List Filter to the admin interface.',
    long_description=README,
    url='https://github.com/ctxis/django-admin-multiple-choice-list-filter',
    author='Patrick Heneghan',
    author_email='git@discopatrick.me',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
