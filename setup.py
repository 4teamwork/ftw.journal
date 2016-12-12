from setuptools import setup, find_packages
import os

version = '1.2.10.dev0'
maintainer = 'Jonas Baumann'

tests_require = [
    'mocker',
    'unittest2',
    'zope.configuration',
    'plone.app.testing',
    'plone.mocktestcase',
    ]

setup(name='ftw.journal',
      version=version,
      maintainer=maintainer,
      description="Journaling infrastructure for plone",

      long_description=open("README.rst").read() + "\n" + \
          open(os.path.join("docs", "HISTORY.txt")).read(),

      # Get more strings from
      # http://www.python.org/pypi?%3Aaction=list_classifiers

      classifiers=[
        'Framework :: Plone',
        'Framework :: Plone :: 4.0',
        'Framework :: Plone :: 4.1',
        'Framework :: Plone :: 4.2',
        'Framework :: Plone :: 4.3',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],

      keywords='plone workflow journal',
      author='4teamwork AG',
      author_email='mailto:info@4teamwork.ch',
      url='https://github.com/4teamwork/ftw.journal',

      license='GPL2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ftw'],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
        'setuptools',

        # Zope
        'Acquisition',
        'zope.annotation',
        'zope.component',
        'zope.event',
        'zope.formlib',
        'zope.i18nmessageid',
        'zope.interface',
        'zope.schema',
        'ZODB3',
        'Zope2',

        # Plone
        'Plone',
        'Products.CMFCore',
        'plone.app.contentrules',
        'plone.contentrules',
        ],

      tests_require=tests_require,
      extras_require = dict(tests=tests_require),

      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
