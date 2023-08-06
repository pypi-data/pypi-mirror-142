from setuptools import setup, find_packages
from codecs import open
from distutils.util import convert_path

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

main_ns = {}
ver_path = convert_path('coinpricli/__init__.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

setup(
    name='coinpricli',
    version=main_ns['__version__'],
    packages=find_packages(include=['coinpricli', 'coinpricli.*']),
    install_requires=[
        'beautifulsoup4>=4.10.0',
        'requests',
        'texttable>=1.6.4',
    ],
    entry_points={
        'console_scripts': ['coinpricli=coinpricli.coinpricli:main']
    },
    setup_requires=['flake8'],
    url='https://github.com/dumpsayamrat/coinpricli',
    keywords="cryptocurrency cli coin coicli",
    license='BSD',
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11"
    ],
    author='Sayamrat Kaewta',
    author_email='sayamrat.kt@gmail.com',
    description='a package where you can easily monitor cryptocurrencies',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
