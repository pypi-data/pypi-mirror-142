from distutils.core import setup
from setuptools import find_packages

setup(name='pylearner',  # 包名
      version='0.0.2',  # 版本号
      description='a package which is developing',
      long_description="",
      author='azkidzz',
      author_email='cszcszcsz@126.com',
      url='',
      install_requires=[],
      license='GNU GPLv3',
      packages=find_packages(),
      platforms=["all"],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: English',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Software Development :: Libraries'
      ],
      data_files=[("packages", [r"G:\pyLearner\pylearner\test.pylearner"])]
      )
