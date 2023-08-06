import setuptools

setuptools.setup(
    name='pydaisi',
    version='0.1.168',
    license='Apache License 2.0',
    description='A Python Interface for the Daisi Platform',
    url='https://github.com/BelmontTechnology/PyDaisi',
    author='BelmontTechnology',
    author_email='john@belmont.tech',
    keywords='Daisi SDK',
    install_requires=[
     'requests',
     'python-dotenv',
     'dill'
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires='>=3.7'
)
