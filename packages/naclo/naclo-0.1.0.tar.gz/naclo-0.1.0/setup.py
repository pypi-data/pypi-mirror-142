from setuptools import setup, find_packages


setup(
    name='naclo',
    version='0.1.0',
    license='MIT',
    author='Jacob Gerlach',
    author_email='jwgerlach00@gmail.com',
    url='https://github.com/jwgerlach00/naclo',
    description='Cleaning toolset for small molecule drug discovery datasets',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'python==3.7',
        'rdkit-pypi',
    ],
)
