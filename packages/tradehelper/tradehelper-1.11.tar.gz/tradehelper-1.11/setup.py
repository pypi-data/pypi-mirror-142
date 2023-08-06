import setuptools

setuptools.setup(
    name='tradehelper',
    version='1.11',
    license='MIT',
    author="preneeshav",
    author_email='preneesh.av@gmail.com ',
    # packages=find_packages('src'),
    # package_dir={'': 'src'},
        packages=setuptools.find_packages(),
    url='https://github.com/preneeshav/tradehelp',
    
    keywords='trade help',
    install_requires=[
          'pandas','datetime'
      ],

)
