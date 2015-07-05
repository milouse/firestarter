#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='firestarter',
      description=("simple launcher for firefox that let's you choose a profile "
                   'with dmenu, then launches it as a separate instance '
                   '(-new-instance'),
      version='∞',
      author='slowpoke',
      author_email='mail+python@slowpoke.io',
      url='https://github.com/slowpoketail/firestarter',
      scripts=['firestarter'],
      install_requires=['plac'],
      classifiers=['Intended Audience :: Developers',
                   'Programming Language :: Python :: 3',
                   'Operating System :: Unix',
                   'License :: Public Domain',
                   'Environment :: X11 Applications',
                   'Development Status :: 5 - Production/Stable'],
      license='ANTI-LICENSE')

