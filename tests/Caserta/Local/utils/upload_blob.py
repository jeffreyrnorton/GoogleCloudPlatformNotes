"""
Script to copy a local file into a GCP storage bucket.
ACLs are not modified in this file.

"""
import sys
# To install the google-api-python-client...
#```> pip install --upgrade google-api-python-client```
from google.cloud import storage
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
import logging

# Set logging environment
FORMAT = '%(asctime)-15s %(levelname)-6s %(message)s'
DATE_FORMAT = '%b %d %H:%M:%S'
logger = logging.getLogger(__name__)
formatter = logging.Formatter(fmt=FORMAT, datefmt=DATE_FORMAT)
# Clear the handlers out
for h in reversed(logger.handlers):
    logger.removeHandler(h)
# Add the one handler that is desired.
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

"""
upload_blob - Uploads a file from the local file system to be a 'blob' on a GCP bucket.

Input:
bucket_name           - name of the bucket
source_file_name      - full path to the local file.
destination_blob_name - Full path of the blob (file) in the GCP bucket.

"""
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    try:

        # Enable api authentication to get application default credentials with the gcloud command line.
        #> gcloud beta auth application-default login
        # Build credentials using environment data set by the command above.
        logger.info('Setting credentials')
        credentials = GoogleCredentials.get_application_default()
        # Build the storage service
        logger.info('Building Storage Service')
        service = discovery.build('storage', 'v1', credentials=credentials)

        # Create the body of call to execute.
        logger.info('Building payload')
        body = {'name': destination_blob_name}
        # Set the data required to upload to the bucket.
        req = service.objects().insert(bucket=bucket_name, body=body, media_body=source_file_name)
        # Execute the call
        logger.info('Executing ...')
        resp = req.execute()
        logger.info('Finished Executing')
    except Exception as e:
        logger.fatal('Failed to load the file with error {}'.format(str(e)))

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("USAGE: {} <bucket_name>, <source_file_name>, <destination_blob_name>".format(sys.argv[0]))
        sys.exit(-1)
    upload_blob(sys.argv[1], sys.argv[2], sys.argv[3])

