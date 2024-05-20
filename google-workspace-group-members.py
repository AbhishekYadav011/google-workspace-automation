from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


def main():
    SERVICE_ACCOUNT_JSON_FILE_PATH = 'credentials.json'
    credentials = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_JSON_FILE_PATH,scopes=['https://www.googleapis.com/auth/admin.directory.group.member'])
    credentials = credentials.create_delegated('delegated_user@gmail.com')
    service = build('admin', 'directory_v1', credentials=credentials)

    # Call the Admin SDK Directory API
    print('Getting the members list in the group')
    results = service.members().list(groupKey='gcp_devops@gmail.com').execute()
    print(results.get('nextPageToken'))
    nextPageToken = results.get('nextPageToken')
    members = results.get('members', [])
    memberlist = open("memberlist.txt", "w+")

    if not members:
        print('No members in the Group.')
    else:
        print('members:')
        for member in members:
            print(member['email'])
            memberlist.write(member['email'] + "\n")
                
    memberlist.close()

    while nextPageToken is not None:
        results = results = service.members().list('gcp_devops@gmail.com',pageToken=nextPageToken).execute()
        members = results.get('members', [])
        memberlist_append = open("userlist.txt", "a+")
        if not members:
            print('No members in the Group.')
        else:
            # print('Members:')
            for member in members:
                print(member['email'])
                memberlist_append.write(member['email'] + "\n")
                    
        if results.get('nextPageToken') is not None:
            # print(results.get('nextPageToken'))
            nextPageToken = results.get('nextPageToken')
        else:
            print("loop done")
            break


if __name__ == '__main__':
    main()
