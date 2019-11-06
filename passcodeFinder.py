from readinOfEmail import ReadEmails

class ParsEmail(ReadEmails):
    def __init__(self):
        ReadEmails.__init__(self)
        self.ParenClas     = ReadEmails()
        self.list_of_email = self.get_emails()
        self.email_to      = ""
        self.passcode      = ""
        self.email_from    = ""

    def find_passcode(self, email_from, email_to, subjec_to_find):
        for message in self.list_of_email:
            msg                = self.ParenClas.service.users().messages().get( userId='me', id=message['id'], format='full').execute() #gets the individual message from email            
            correct_email_from = False
            correct_email_to   = False
            correct_subject    = False
            for email_subject in msg['payload']['headers']:
                if email_subject['name'] == 'From'    and email_subject['value'] == email_from:     correct_email_from = True
                if email_subject['name'] == 'To'      and email_subject['value'] == email_to:       correct_email_to   = True
                if email_subject['name'] == 'Subject' and email_subject['value'] == subjec_to_find: correct_subject    = True
            if correct_email_from and correct_email_to and correct_subject:
                return msg['snippet'].split('|')[0].split(',')[0].split(':')[1].split(" ")[1] # it's the code for confirmation