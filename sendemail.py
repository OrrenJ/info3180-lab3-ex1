import smtplib

from_addr = ''
to_addr = ''
subject = 'This is a Test'
msg = "If you're seeing this, then everything worked fine. :D"
message = 'Subject: {}\n\n{}'

message_to_send = message.format(subject, msg)

# Credentials (if needed)
username = ''
password = ''

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit()