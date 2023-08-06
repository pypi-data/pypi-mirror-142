from distutils.core import setup
from setuptools import find_packages

with open("README.rst", "r") as f:
    long_description = f.read()

setup(name='FSE22_CAT',  # 包名
      version='0.0.1',  # 版本号
      description='an automated data cleaning tool for code summarization datasets',
      long_description=long_description,
      author='FSE22_built_on_the_rock',
      author_email='FSE22_built_on_the_rock@outlook.com',
      url='https://github.com/BuiltOntheRock/FSE22_BuiltOntheRock',
      install_requires=[],
      license='BSD License',
      packages=find_packages(),
      platforms=["all"],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
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
      )
