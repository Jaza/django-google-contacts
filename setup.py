from setuptools import setup, find_packages
 
setup(name='django-google-contacts',
    version='0.1',
    description='Retrieve contacts from the Gmail account of a user of your Django site',
    long_description=open('README.txt').read(),
    author='Jeremy Epstein',
    author_email='je@digitaleskimo.net',
    url='http://github.com/Jaza/django-google-contacts',
    packages=find_packages(),
    classifiers=[
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
    ]
)
