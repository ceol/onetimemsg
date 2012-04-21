# Most of this format was swiped from the `alchemy` Pyramid paster.

import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requires = [
    'Flask',
    'Flask-Script',
    'Flask-WTF',
    'SQLAlchemy',
]

setup(name='OneTimeMsg',
      version='0.0',
      description='A web app for sending self-destructing messages.',
      long_description=open(os.path.join(here, 'README.md')).read(),
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Flask",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      zip_safe=False,
      author='Patrick Jacobs',
      author_email='ceolwulf@gmail.com',
      url='https://github.com/ceol/onetimemsg',
      keywords='flask wsgi messaging',
      packages=find_packages(),
      include_package_data=True,
      install_requires=requires,
      )