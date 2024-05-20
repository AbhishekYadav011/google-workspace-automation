from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


def main():
    SERVICE_ACCOUNT_JSON_FILE_PATH = 'credentials.json'
    credentials = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_JSON_FILE_PATH,scopes=['https://www.googleapis.com/auth/admin.directory.user'])
    credentials = credentials.create_delegated('delegated_user@gmail.com')
    service = build('admin', 'directory_v1', credentials=credentials)

    # Call the Admin SDK Directory API
    print('Getting the users list in the domain')
    results = service.users().list(customer='my_customer',
                                   orderBy='email').execute()
    print(results.get('nextPageToken'))
    nextPageToken = results.get('nextPageToken')
    users = results.get('users', [])
    userlist = open("userlist.txt", "w+")

    if not users:
        print('No users in the domain.')
    else:
        print('Users:')
        for user in users:
            if not user['suspended']:
                print(user)
                userlist.write(user['primaryEmail'] + "\n")
                
    userlist.close()

    while nextPageToken is not None:
        results = service.users().list(customer='my_customer',
                                       orderBy='email', pageToken=nextPageToken).execute()
        users = results.get('users', [])
        userlist_append = open("userlist.txt", "a+")
        if not users:
            print('No users in the domain.')
        else:
            # print('Users:')
            for user in users:
                if not user['suspended']:
                    print(user)
                    userlist_append.write(user['primaryEmail'] + "\n")
              
                            

        if results.get('nextPageToken') is not None:
            # print(results.get('nextPageToken'))
            nextPageToken = results.get('nextPageToken')
        else:
            print("loop done")
            break


if __name__ == '__main__':
    main()
