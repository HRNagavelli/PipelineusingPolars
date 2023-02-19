"""Connector Module to Connect to S3 Bucket Resource"""
import logging
import boto3
from secrets_connector import aws_SecretsManager


class s3Bucket_Connector():
    """
    Class for communicating with S3 Bucket 
    """
    aws_Secrets = aws_SecretsManager.get_secret()
    access_key = aws_Secrets['Access key ID']
    secret_key = aws_Secrets['Secret access key']
    def __init__(self,access_key:str , secret_key:str,endpoint_url:str, bucket:str):
        """
        Constructor for S3 Bucket Connector

        :param access_key: Used to Access S3 Bucket 
        :param secret_key: Used to Authenticate S3 Bucket
        :param endpoint_url: endpoint URL to Commnicate with S3
        :param bucket: S3 Bucket Name
        """
        self._logger = logging.getLogger(__name__)
        self.endpoint_url = endpoint_url
        self.session = boto3.Session(aws_access_key_id=access_key,aws_secret_access_key=secret_key)
        self._s3 = self.session.resource (service_name='s3',endpoint_url= endpoint_url)
        self._bucket = self._s3.Bucket(bucket)

    def list_files_using_filter(self,prefix: str):
        """
        Listing all the files using a prefix provided 

        :param prefix: prefix on the s3 bucket that should be filtered with

        returns:
            files: list of all the file names containing the prefix in the key
        """
        files = [obj.key for obj in self._bucket.objects.filter(Prefix=prefix)]
        return files
    def load_data_from_s3(self):
        pass
    def write_back_data_to_s3(self):
        pass
    