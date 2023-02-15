"""Connector Module to Connect to AWS Secrets Manager and Fetch the AWS Secrets"""


import boto3



import boto3
import json
from botocore.exceptions import ClientError


class aws_SecretsManager():
    """
    Class to Communicate with AWS Secret Manager and Get the Secrets stored
    """
    def get_secret():

        secret_name = "S3AccessKeys"
        region_name = "us-east-2"

        # Create a Secrets Manager client
        session = boto3.session.Session()
        client = session.client(
            service_name='secretsmanager',
            region_name=region_name
        )

        try:
            get_secret_value_response = client.get_secret_value(
                SecretId=secret_name
            )
        except ClientError as e:
            # For a list of exceptions thrown, see
            # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
            raise e

        # Decrypts secret using the associated KMS key.
        secret_string = get_secret_value_response['SecretString']
        secret_json = json.loads(secret_string)
        return secret_json
    # Your code goes here.