# s3_connection

## Description

A package that allows an easy connection to be made to an [AWS S3](https://docs.aws.amazon.com/s3/index.html) bucket, provided a valid [AWS Access Key & AWS Secret Key](https://docs.aws.amazon.com/general/latest/gr/aws-security-credentials.html) are given (if no credentials are provided then only public buckets can be accessed). The package contains a class which stores the keys provided, and allows the user to read/write certain file formats to/from s3 buckets, through the use of class methods.

This package is essentially a wrapper for the [s3fs package](https://s3fs.readthedocs.io/en/latest/index.html). It was created to be used as a subpackage in a wider project - PSUSANNX.

### Package Functions

- read_csv_from_s3()
- write_csv_to_s3()
- read_json_from_s3()
- write_json_to_s3()
- read_h5_from_s3()
- write_h5_to_s3()
- read_pkl_from_s3()
- write_pkl_to_s3()

## Installation

```python
pip install s3_connection
```

## Usage

```python
# Import the class object from the package
from s3_connection.s3_conn_class import S3Connection

# Get some info about the class object
help S3Connection 
```

Once the class has been imported and you've read the help, you can create an instance of the class to allow you to interact with an s3 bucket in your aws account. Make sure you have the AWS Access key & the AWS secret key at hand.

```python
# Create an instance of the class with AWS credentials
s3_conn = S3Connection(
    aws_access_key='<AWS-ACCESS-KEY>', 
    aws_secret_key='<AWS-SECRET-KEY>'
    )
```

The s3_conn object can now be used to call the functions to read/write to s3 buckets.

If you dont have access or secret keys and you want to access objects in **public buckets**, all you need to do is instantiate an instance of the class with no arguments, like this.

```python
# Create an instance of the class with no credentials
s3_conn = S3Connection()
```

## The *read_from_s3* functions

The read___from_s3 functions just take the bucket name & object name as arguments then return the object.

```python
# Use the s3_conn to read a csv from a bucket
pandas_df = s3_conn.read_csv_from_s3(
    bucket_name="<bucket-name>", 
    object_name="<path/to/file/within/bucket.csv>"
    )
```

## The *write_to_s3* functions

The write___to_s3 functions take the bucket name, object name & the data as arguments and return nothing.

If you already have a dataframe stored in a variable called existing_df then you can put it into an s3 bucket with the following function (index=False is automatically applied).

```python
# Put the existing_df dataframe into the s3 bucket as a csv file
s3_conn.write_csv_to_s3(
    bucket_name="<bucket-name>", 
    object_name="<path/to/save/file.csv>",
    data=existing_df
    )
```

## Notes

- The package is quite restricted in what it can do, but it only needs to do things that are required by the parent project so there won't be much development.
- A potential new feature to add to the package would be the ability to manage S3 resources, like create/delete buckets & objects from S3 from within the package.
