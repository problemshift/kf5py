from setuptools import setup

setup(
    name='kf5connection',
    version='0.1.dev1',
    author='Chris Teplovs',
    author_email='dr.chris@problemshift.com',
    url='http://pypi.python.org/pypi/kf5connection/',
    license='LICENSE.txt',
    description='Connection utilities for KF5.',
    long_description=open('README.txt').read(),
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
