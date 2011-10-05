from setuptools import setup, find_packages
import os

version = open('ftw/journal/version.txt').read().strip()
maintainer = 'Jonas Baumann'
tests_require = ['plone.app.testing',
                 'plone.mocktestcase',]
setup(name='ftw.journal',
      version=version,
      description="Journaling infrastructure (Maintainer: %s)" % maintainer,
      long_description=open("README.txt").read() + "\n" + \
          open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone ftw workflow journal',
      author='%s, 4teamwork GmbH' % maintainer,
      author_email='mailto:info@4teamwork.ch',
      url='http://psc.4teamwork.ch/4teamwork/ftw/ftw.journal',
      license='GPL2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ftw'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        ],
      tests_require=tests_require,
      extras_require = dict(tests=tests_require),

      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = opengever
      """,
      )
