import gspread
from oauth2client.service_account import ServiceAccountCredentials
from send import send_message
from message_template import make_message

scope=["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds=ServiceAccountCredentials.from_json_keyfile_name('credentials.json',scope)
client=gspread.authorize(creds)
sheet=client.open('tutorialss').sheet1
data=sheet.get_all_records()
col=sheet.col_values(3)
col=col[1:]



if __name__=='__main__':
    l=['acchaladka1729@gmail.com','acchaladka1729@gmail.com','acchaladka1729@gmail.com']
    send_message(to_email=l)
    
