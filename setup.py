from setuptools import setup, find_packages
import os

version = '0.2.3'

setup(name='ftw.journal',
      version=version,
      description="Journaling infrastructure",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone ftw workflow journal',
      author='Christian Schneider, 4teamwork GmbH',
      author_email='christian.schneider@4teamwork.ch',
      url='https://svn.4teamwork.ch/repos/ftw/ftw.journal',
      license='Copyright 2009, 4teamwork GmbH',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ftw'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
