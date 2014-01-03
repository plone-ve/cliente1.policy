from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='cliente1.policy',
      version=version,
      description="Plone site policy for Cliente1 website",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone policy package cliente1 website',
      author='Leonardo J. Caballero G.',
      author_email='plone-developers@lists.sourceforge.net',
      url='https://github.com/collective/cliente1.policy',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['cliente1'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
