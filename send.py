import smtplib
from cred import username,password  
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from message_template import make_message


def send_message(from_email='acchaladka1729@gmail.com',to_email=['acchaladka1729@gmail.com'],msg_string=make_message("USER","YOUR_EMAIL")):
    msg=MIMEMultipart('alternative')
    msg['From']=from_email
    msg['Subject']="WOW SUCHA A NICE SUBJECT"
    
    text_part=MIMEText(msg_string,'plain')
    msg.attach(text_part)
    
    server=smtplib.SMTP(host='smtp.gmail.com',port=587)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    for items in to_email:
        msg['To']=items
        msg_string=msg.as_string()
        print("sending...",end=" ")
        try:
            server.sendmail(from_email,items,msg_string)
            print('DONE!!!')
        except:
            print("INVALID EMAIL-ID")
        del msg['To']
        
        
    server.quit()

