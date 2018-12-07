import smtplib

# Note: if you want to use this you need to enable your gmail account to be accessed by less
# secure apps- just do a quick google search

# Your email account information
username = ""
password = ""

# Where you want to send the email
targetEmail = ""

def sendEmail(msg):
    # this is the server if you are using a gmail account to send the message (recommended)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Next, log in to the server
    server.login(username, password)

    # Send the mail
    msgToSend = "User, \n" \
          "The dehumidifier has issued the following alert: \n" \
          "\t-"+msg+"\n" \
                    "Have a nice day!" # The /n separates the message from the headers
    server.sendmail(username, targetEmail, msgToSend)
    print("Email sent!")
    return 0
