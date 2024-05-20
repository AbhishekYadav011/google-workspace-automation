# google-workspace-automation
This repo is created to get the user list of entire org , list of members from a group in workspace and list of org unit in workspace from G-suite using Workspace Admin SDK

## To install the Google client library for Python, run the following command:
>  pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

## Set the value of below [varibales](https://developers.google.com/admin-sdk/directory/v1/guides/delegation#python) before executing this code:
1. Delegated email id
2. SERVICE_ACCOUNT_JSON_FILE_PATH = 'Json file path'
3. scopes=['https://www.googleapis.com/auth/admin.directory.user','https://www.googleapis.com/auth/admin.directory.orgunit','https://www.googleapis.com/auth/admin.directory.group.member']
