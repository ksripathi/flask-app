
from setuptools import setup

requires = [
    'flask',
    'Flask-SQLAlchemy',
    'oursql',
    'flask-cors',
    'flask-testing',
    'requests'
]

setup(
    name='flask-demo',
    version='2.0',
    install_requires=requires
)
