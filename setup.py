# -*- coding: utf-8 -*-
"""
This module contains the tool of pwrentch.FileReferences
"""
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '1.0'

long_description = (
    read('README.md')
    + '\n' +
    'Change history\n'
    '**************\n'
    + '\n' +
    read('CHANGES.md')
    )

tests_require = ['zope.testing']

setup(name='pwrentch.FileReferences',
      version=version,
      description="Lists file and image items and the items that link to them",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='',
      author='Paul Rentschler',
      author_email='paul@rentschler.ws',
      url='https://github.com/paulrentschler/pwrentch.FileReferences',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['pwrentch', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        # -*- Extra requirements: -*-
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite='pwrentch.FileReferences.tests.test_docs.test_suite',
      entry_points="""
      # -*- entry_points -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
