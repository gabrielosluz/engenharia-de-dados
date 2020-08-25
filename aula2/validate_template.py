import boto3
import logging
from botocore.exceptions import ClientError
import os

logging.getLogger().setLevel(logging.INFO)
client = boto3.client('cloudformation')

with open('glue.yml', 'r') as f:
    template = f.read()

response = client.validate_template{
    TemplateBody= template
}

print(response)