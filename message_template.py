message_temp="""Hello {name} How are you??\nAn Email has been sent to {email_id}"""

def make_message(make_name="NONAME",make_email_id="NOEMAIL-ID"):
   return message_temp.format(name=make_name,email_id=make_email_id)


