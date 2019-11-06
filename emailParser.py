
testEmaila = ReadEmails()
# for email in testEmaila.get_emails():
#     print(email.values)
for message in testEmaila.get_emails():
    msg = testEmaila.service.users().messages().get(userId='me', id=message['id'],format='full').execute()
    for email_subject in msg['payload']['headers']:
        # print(email_subject)
        if email_subject['name'] == 'From' and email_subject['value'] == 'Webnovel <noreply@webnovel.com>':
            print(email_subject['value'])
            print(msg['snippet'])
            # print(email_subject)
            # print(msg['payload']['parts']['0']['body']['data'])
            time.sleep(10)
            #  print(msg['body'])