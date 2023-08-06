from setuptools import setup, find_packages


setup(
    name='naclo',
    version='0.1.3',
    license='MIT',
    author='Jacob Gerlach',
    author_email='jwgerlach00@gmail.com',
    url='https://github.com/jwgerlach00/naclo',
    description='Cleaning toolset for small molecule drug discovery datasets',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    python_requires='>=3.6, <3.8',
    install_requires=[
        'rdkit-pypi',
    ],
)
