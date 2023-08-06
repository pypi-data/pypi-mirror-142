from setuptools import setup, find_packages
from pathlib import Path


current_dir = Path(__file__).parent
long_description = (current_dir / "README.md").read_text()

# Set up the package metadata
setup(
    name="s3_connection",
    author="Jamie O'Brien",
    description="A package with functions for reading/writing different file types from/to AWS S3 storage. It is essentially a wrapper for the s3fs package.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    version="0.1.2",
    packages=find_packages(include=["s3_connection", "s3_connection.*"]),
    install_requires=[
        's3fs>=2022.2.0',
        'tensorflow>=2.8.0',
        'pandas>=1.3.4'
        ]
)