#!/usr/bin/python3
# written by: atholcomb
# Script uploads the wp-content direcotry into Google Drive

import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from Google import Create_Service
from google.oauth2 import service_account

CLIENT_SVC_FILE = 'svc-key.json'
SCOPES = ['https://www.googleapis.com/auth/drive.file']
API_NAME = 'drive'
API_VERSION = 'v3'

# Specify Service Account key credentials
CREDS = service_account.Credentials.from_service_account_file(CLIENT_SVC_FILE, scopes=SCOPES)

# Create service object
service = build(API_NAME, API_VERSION, credentials=CREDS)

# Upload into haetal root folder
folder_id = "1QN3xsd6wdZszY-HlIn_1A4h-FGKTD5Ey"

# Start the upload process
print("Uploading file(s)...")
file_metadata = {
  'name': ['wordpress_backup.sql'],
  'parents': [folder_id]
}
 
# Create the upload criteria for the wp-contents zip directory (uncomment when uploading zip)
#media = MediaFileUpload('8p_wp-content.zip',  mimetype='application/zip')

# Create the upload criteria for the database backup
media = MediaFileUpload('wordpress_backup.sql',  mimetype='application/vnd.oasis.opendocument.database')

# Call the service object and execute the upload
service.files().create(body=file_metadata, media_body=media, fields='id').execute()

# Tell us when it's done
print("Done")

