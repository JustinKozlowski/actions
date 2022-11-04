import setuptools

setuptools.setup(
    name='simplepythontest',
    version='0.0.1',
    description='Simple Unit Test Demo',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    python_requires='>=3.6, <4',
)
