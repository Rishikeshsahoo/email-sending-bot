import imaplib
import email
from cred import username,password
host='imap.gmail.com'

mail=imaplib.IMAP4_SSL(host)
mail.login(username,password)
mail.select('inbox')

_,search_data=mail.search(None,"UNSEEN")


for maildata in search_data[0].split():
    _,data=mail.fetch(maildata,'(RFC822)')
    _,b=data[0]
    email_message=email.message_from_bytes(b)
    msg="{} : {}"
    L=['from','to','subject','date']
    for things in L:
        print(msg.format(things,email_message[things]))
    for email_part in email_message.walk():
        if(email_part.get_content_type()=='text/plain'):
            body=email_part.get_payload(decode=True)
            print("\n"+body.decode()+"\n\n")


