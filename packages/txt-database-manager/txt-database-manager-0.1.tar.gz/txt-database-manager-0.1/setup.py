from setuptools import setup, find_packages


setup(
    name='txt-database-manager',
    version='0.1',
    license='MIT',
    author="Hugo Coto",
    author_email='hugocoto100305@example.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/hugoocf/txtdatabase',
    keywords='txt database manager',
    install_requires=[],

)