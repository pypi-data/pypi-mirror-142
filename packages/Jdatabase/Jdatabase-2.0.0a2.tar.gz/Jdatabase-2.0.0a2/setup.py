from setuptools import setup, find_packages
from current_version_grabber import current_version

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='Jdatabase',
      version=current_version,
      packages=['Jdatabase'],
      license='MIT',
      description='Jdatabase Python package. Designed for ease of database control and interaction within Python. The Jdatabase package supports MySQL and PostgreSQL database systems.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      install_requires=['mysqlclient', 'psycopg2-binary'],
      url='https://github.com/JoshWidrick/jdb',
      author='Joshua Widrick',
      author_email='joshua.widrick@gmail.com',
)

