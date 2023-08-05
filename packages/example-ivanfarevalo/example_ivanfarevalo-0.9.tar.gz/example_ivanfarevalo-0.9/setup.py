from setuptools import setup, find_packages


setup(
    name='example_ivanfarevalo',
    version='0.9',
    license='MIT',
    author="Ivan Arevalo",
    author_email='ivan.felipe.ag@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='example project',
    install_requires=[
          'scikit-learn',
      ],

)
