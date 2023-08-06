from setuptools import setup, find_packages


setup(
    name='tradehelper',
    version='1.0',
    license='MIT',
    author="preneeshav",
    author_email='preneesh.av@gmail.com ',
    packages=find_packages('src'),
    # package_dir={'': 'src'},
    url='https://github.com/preneeshav/tradehelp',
    keywords='trade help',
    install_requires=[
          'pandas','datetime'
      ],

)
