import setuptools

setuptools.setup(
    name='example-cicd-web-app',
    author='Snow Storm',
    author_email='jkozlowski1@mtb.com',
    version='0.0.1',
    description='api website',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    python_requires='>=3.6, <4',
)
