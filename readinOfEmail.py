from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

class ReadEmails:
    def __init__(self, scope='https://www.googleapis.com/auth/gmail.readonly', jsonLocation='F:\\python\\automateWork\\credentials.json'):
        self.SCOPES = scope
        self.store  = file.Storage('token.json')
        self.creds  = self.store.get()

        if not self.creds or self.creds.invalid:
            flow       = client.flow_from_clientsecrets(jsonLocation, self.SCOPES)
            self.creds = tools.run_flow(flow, self.store)
        self.service   = build('gmail', 'v1', http=self.creds.authorize(Http() ) )
    def get_emails(self):
        # Call the Gmail API to fetch INBOX
        results = self.service.users().messages().list(userId='me', labelIds=['INBOX']).execute() # returns all IDS of emails labled as INBOX        
        return results.get('messages', [])