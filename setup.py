from setuptools import setup

setup(
    name='kf5py',
    version='0.1.dev1',
    author='Chris Teplovs',
    author_email='dr.chris@problemshift.com',
    url='http://pypi.python.org/pypi/kf5py/',
    license='LICENSE.txt',
    description='Python-based utilities for KF5.',
    long_description=open('README.md').read(),
    install_requires=[
        "requests >= 2.3.0"
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
