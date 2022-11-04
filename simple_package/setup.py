import setuptools

setuptools.setup(
    name='simple-python-package',
    version='0.0.1',
    description='Simple Package Demo',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    python_requires='>=3.6, <4',
)
