from setuptools import setup, find_packages


setup(
    name='example_ivanfarevalo',
    version='1.0',
    license='MIT',
    author="Ivan Arevalo",
    author_email='ivan.felipe.ag@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='example project',
    install_requires=[
          'scikit-learn==0.24.1',
      ],

)
