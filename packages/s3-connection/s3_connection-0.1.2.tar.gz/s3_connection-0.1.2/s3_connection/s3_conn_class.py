"""The class that will store the aws access & secret keys for convenience"""

# Import packages
import pandas as pd
import pickle as pkl
import json
import s3fs
from tensorflow.keras.models import load_model
import os


class S3Connection():

    """The class that brings together all the s3 connection functions."""

    def __init__(self, aws_access_key=None, aws_secret_key=None):
        
        """
        Use the credentials to set up a connection to an S3 bucket on creation of the class instance.

        Parameters
        ----------
        aws_access_key: str
            The access key associated with the account you want to use to connect to s3.

        aws_secret_key: str
            The secret key associated with the account you want to use to connect to s3.
        """

        if (aws_access_key is None) or (aws_secret_key is None):
            print("If you want to access private S3 buckets, you will need to provide valid AWS secret & access keys.\nOtherwise you can only access public buckets.")
        
        # create the connection to s3 and store it in the class instance     
        self.s3 = s3fs.S3FileSystem(anon=False, key=aws_access_key, secret=aws_secret_key)


    def read_csv_from_s3(self, bucket_name, object_name):

        """
        Read a csv file from s3 as a pandas DataFrame.
        
        Parameters
        ----------
        bucket_name: str
            The name of the bucket the data should be read from.

        object_name: str
            The path to the object within the bucket. eg "folder/subfolder/file.csv"
        
        Returns
        -------
        Pandas DataFrame object
        """

        # Open the file and read the csv through pandas
        data = pd.read_csv(self.s3.open(f"{bucket_name}/{object_name}", "rb"))

        return data


    def write_csv_to_s3(self, bucket_name, object_name, data):

        """
        Write a pandas DataFrame to a csv in s3.
        
        Parameters
        ----------
        bucket_name: str
            The name of the bucket the data should be written to.

        object_name: str
            The path to the object within the bucket. eg "folder/subfolder/file.csv"
        
        data: pandas.DataFrame
            The dataframe object to be saved to a csv.

        Returns
        -------
        None
        """

        # Write the pandas dataframe to a csv in the s3 bucket
        data.to_csv(self.s3.open(f"{bucket_name}/{object_name}", "w"), index=False)


    def read_json_from_s3(self, bucket_name, object_name):

        """
        Read a json file from s3.
        
        Parameters
        ----------
        bucket_name: str
            The name of the bucket the data should be written to.

        object_name: str
            The path to the json file within the bucket. eg "folder/subfolder/file.json"

        Returns
        -------
        dict
        """

        # Extract the data from the s3 object
        data = json.load(self.s3.open(f"{bucket_name}/{object_name}"))

        return data
    
    
    def write_json_to_s3(self, bucket_name, object_name, data):

        """
        Write a json file to s3.
        
        Parameters
        ----------
        bucket_name: str
            The name of the bucket the data should be written to.

        object_name: str
            The path to the json file within the bucket. eg "folder/subfolder/file.json"

        Returns
        -------
        None
        """
        
        # Put the json object in the s3 bucket
        json.dump(data, self.s3.open(f"{bucket_name}/{object_name}",'w'))
        

    def write_h5_to_s3(self, bucket_name, object_name, data):

        """
        Write a keras model object (.h5 extension) to s3.
        
        Parameters
        ----------
        model_object: keras model object
            A trained keras model object.

        bucket_name: str
            The name of the bucket the data should be written to.

        object_name: str
            The path to the json file within the bucket. eg "folder/subfolder/file.json"
        
        Returns
        -------
        None
        """

        # First save the model to the local directory, to be copied to s3
        data.save(object_name)

        # Put the model into s3
        self.s3.put(object_name, f"{bucket_name}/{object_name}")
        
        # Remove the model object file from the local directory
        os.remove(object_name)


    def read_h5_from_s3(self, bucket_name, object_name):

        """
        Read a h5 model object from s3.
        
        Parameters
        ----------
        bucket_name: str
            The name of the bucket the model object should be read from.

        object_name: str
            The path to the .h5 model object file within the bucket. eg "folder/subfolder/model_name.h5"
        
        Returns
        -------
        A keras model object
        """

        # Copy the model object file to the local directory
        self.s3.get(f"{bucket_name}/{object_name}", object_name)

        # Read in the model that has been copied from s3
        data = load_model(object_name)

        # Remove the model object file from the local directory
        os.remove(object_name)

        return data


    def write_pkl_to_s3(self, bucket_name, object_name, data):
        
        """
        Write a pickled object (.pkl extension) to s3.
        
        Parameters
        ----------
        pkl_object: a pickled object
            A pickled object.

        bucket_name: str
            The name of the bucket the object should be written to.

        object_name: str
            The path to the json file within the bucket. eg "folder/subfolder/object.pkl"
        
        Returns
        -------
        None
        """

        # First save the model to the local directory, to be copied to s3
        pkl.dump(data, self.s3.open(f"{bucket_name}/{object_name}", 'wb'))


    def read_pkl_from_s3(self, bucket_name, object_name):
        
        """
        Read a pickled object (.pkl extension) from s3.
        
        Parameters
        ----------
        bucket_name: str
            The name of the bucket the .pkl file should be read from.

        object_name: str
            The path to .pkl object within the bucket. eg "folder/subfolder/file.pkl"
        
        Returns
        -------
        An unpickled object to be used
        """

        # Read in the pkl data from s3
        data = pkl.load(self.s3.open(f"{bucket_name}/{object_name}", 'rb'))

        return data