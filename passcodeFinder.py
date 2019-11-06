from readinOfEmail import ReadEmails
import time

class ParsEmail(ReadEmails):
    def __init__(self):        
        ReadEmails.__init__(self)
        self.ParenClas = ReadEmails()
        self.list_of_email = self.get_emails()
    def find_passcode(self):
        for message in self.list_of_email:
            msg = self.ParenClas.service.users().messages().get(userId='me', id=message['id'],format='full').execute()
            for email_subject in msg['payload']['headers']:
                # print(email_subject)
                if email_subject['name'] == 'From' and email_subject['value'] == 'Webnovel <noreply@webnovel.com>':
                    print(email_subject['value'])
                    print(msg['snippet'])
                    # print(email_subject)
                    # print(msg['payload']['parts']['0']['body']['data'])
                    time.sleep(10)
test = ParsEmail()
test.find_passcode()