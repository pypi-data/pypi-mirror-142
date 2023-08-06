import os
from setuptools import setup, find_packages

def read(*pathnames):
    return open(os.path.join(os.path.dirname(__file__), *pathnames)).read()

version = '1.4.1'

setup(
    name='collective.portletmetadata',
    version=version,
    description="Adds metadata functionality to portlets",
    long_description='\n'.join([
        read('README.rst'),
        read('CHANGES.rst'),
    ]),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "Framework :: Plone :: 5.2",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords='portlets metadata class',
    author='Bo Simonsen',
    author_email='bo@headnet.dk',
    url='http://github.com/collective/collective.portletmetadata',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'collective.monkeypatcher',
        'plone.portlets',
        'plone.app.portlets>=3.0.0',
        'setuptools',
        'z3c.jbot',
        'z3c.unconfigure>=1.0.1',
        # -*- Extra requirements: -*-
    ],
    entry_points="""
        # -*- Entry points: -*-
        [z3c.autoinclude.plugin]
        target = plone
    """,
)
