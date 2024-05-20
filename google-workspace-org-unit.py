from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

class createservice:
    SERVICE_ACCOUNT_JSON_FILE_PATH = 'credentials.json'
    credentials = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_JSON_FILE_PATH,scopes=['https://www.googleapis.com/auth/admin.directory.orgunit','https://www.googleapis.com/auth/admin.directory.user'])
    credentials = credentials.create_delegated('delegated_user@gmail.com')
    service = build('admin', 'directory_v1', credentials=credentials)

def add_user_in_OU():
    # Call the Admin SDK Directory API
    print('Getting the OU list in the domain')
    results = service.orgunits().list(customerId='my_customer').execute()
    print(results)
    body ={
        "primaryEmail":"test1@gmail.com",
        "orgUnitPath":"/testou",
    }
    addmemberResult= createservice.service.users().patch(userKey='test1@gmail.com',body=body).execute()
    print(addmemberResult)

def remove_user_in_OU():
    body ={
        "primaryEmail":"test1@gmail.com",
        "orgUnitPath":"/",
    }
    addmemberResult= createservice.service.users().patch(userKey='test1@gmail.com',body=body).execute()
    print(addmemberResult)




if __name__ == '__main__':
    add_user_in_OU()
    remove_user_in_OU()
