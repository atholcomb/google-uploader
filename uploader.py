#!/usr/bin/python3
# written by: atholcomb
# Script uploads the following into Google Drive:
# 1. wp-content direcotry
# 2. Wordpress SQL database
# 3. PHP config file

import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from Google import Create_Service
from google.oauth2 import service_account

def uploader(filetype, name):
  CLIENT_SVC_FILE = 'svc-key.json'
  SCOPES = ['https://www.googleapis.com/auth/drive.file']
  API_NAME = 'drive'
  API_VERSION = 'v3'

  # Specify Service Account key credentials
  CREDS = service_account.Credentials.from_service_account_file(CLIENT_SVC_FILE, scopes=SCOPES)

  # Create service object
  service = build(API_NAME, API_VERSION, credentials=CREDS)

  # Upload into the 8thpath root folder
  zip_folder_id = '17xQLUIuDk6EDJ9u6nD5IRmfKiMUvMx_I'
  sql_folder_id = '12d0VwNkRdvN9h4_GSMZS_OB2qaBw5dVY'
  config_folder_id = '1K7Q9Y7HUTWVYQN9LWde6bI1d8yRSuzRG'

  ### Start the ZIP upload process ###
  if filetype == "zip":
    print("Uploading zip archive...", end='')
    file_metadata = {
      'name': [name],
      'parents': [zip_folder_id]
    }
      
    media = MediaFileUpload('files/zips/wp-content.zip',  mimetype='application/zip')
    service.files().create(body=file_metadata, media_body=media, fields='id').execute()

    # Tell us when it's done
    print("Done")

  #### Start the SQL upload process ###
  if filetype == "sql":
    print("Uploading SQL database...", end='')
    file_metadata = {
      'name': [name],
      'parents': [sql_folder_id]
    }
      
    media = MediaFileUpload('files/sql/wordpress.sql',  mimetype='application/vnd.oasis.opendocument.database')
    service.files().create(body=file_metadata, media_body=media, fields='id').execute()

    # Tell us when it's done
    print("Done")

  ### Start the CONFIG upload process ###
  if filetype == "config":
    print("Uploading PHP config file...", end='')
    file_metadata = {
      'name': [name],
      'parents': [config_folder_id]
    }
      
    media = MediaFileUpload('files/configs/wp-config.php',  mimetype='text/plain')
    service.files().create(body=file_metadata, media_body=media, fields='id').execute()

    # Tell us when it's done
    print("Done")

def main():
  uploader("zip", "wp-content.zip")
  uploader("config", "wp-config.php")
  uploader("sql", "wordpress.sql")

main()
