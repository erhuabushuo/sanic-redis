"""
    setup
    ~~~~
    A Redis extension for Sanic
    :copyright: (c) 2017 by Aidan (based on aioredis).
    :license: MIT, see LICENSE for more details.
"""

from setuptools import setup
from os.path import join, dirname

with open(join(dirname(__file__), 'sanic_redis/version.py'), 'r') as f:
    exec(f.read())

with open(join(dirname(__file__), 'requirements.txt'), 'r') as f:
    install_requires = f.read().split("\n")


setup(
    name='Sanic-Redis',
    version=__version__,
    url='https://github.com/erhuabshuo/sanic-redis',
    license='MIT',
    author='Aidan',
    author_email='erhuabushuo@gmail.com',
    description="Redis extension for Sanic based on aioredis.",
    long_description=open('README.md').read(),
    packages=['sanic_redis'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=install_requires,
    tests_require=[
        'nose'
    ],
    test_suite='nose.collector',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)