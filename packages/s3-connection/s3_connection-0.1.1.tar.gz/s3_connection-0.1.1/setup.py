from setuptools import setup, find_packages

# Set up the package metadata
setup(
    author="Jamie O'Brien",
    description="A package with functions for reading/writing different file types from/to AWS S3 storage. It is essentially a wrapper for the s3fs package.",
    name="s3_connection",
    version="0.1.1",
    packages=find_packages(include=["s3_connection", "s3_connection.*"]),
    install_requires=[
        's3fs>=2022.2.0',
        'tensorflow>=2.8.0',
        'pandas>=1.3.4'
        ]
)