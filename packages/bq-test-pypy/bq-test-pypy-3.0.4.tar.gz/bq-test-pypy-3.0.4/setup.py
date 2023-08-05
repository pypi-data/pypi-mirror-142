from setuptools import setup, find_packages


setup(
    name='bq-test-pypy',
    version='3.0.4',
    license='MIT',
    author="Bisque Team",
    author_email='ifa@ucsb.edu',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='example project',
    install_requires=[
          'six', 'lxml', 'requests==2.10.0', 'requests-toolbelt',
      ],

)
