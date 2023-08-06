from setuptools import setup

setup(
    name='django-authsignals',
    version='0.1.0',
    description='Consolidate common auth signal behavior',
    author='Nik Nyby',
    author_email='ctl-dev@columbia.edu',
    url='https://github.com/ccnmtl/django-authsignals',
    install_requires=['Django'],
    packages=['authsignals'],
)
