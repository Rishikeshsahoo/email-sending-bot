from message_template import make_message
from send import send_message
import sys

a=sys.argv 
length=len(a)

if (length==2):
    send_message(msg_string=make_message(a[1]))
elif (length>2):
    send_message(msg_string=make_message(a[1],a[2]))
elif(length==1):
    send_message(msg_string=make_message())

    