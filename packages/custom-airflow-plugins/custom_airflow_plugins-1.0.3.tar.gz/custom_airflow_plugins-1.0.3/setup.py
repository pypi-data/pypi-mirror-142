from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='custom_airflow_plugins',
    packages=find_packages(),
    version='1.0.3',
    license='MIT',
    description='Custom airflow 1.X plugins',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Victor Outtes',
    author_email='victor.outtes@gmail.com',
    # url='',
    # download_url='',
    keywords=['airflow', 'plugins'],
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
