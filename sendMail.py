#! python3
# Login to SMTP and send email

import smtplib

def sendEmail (myEmail, password, to, subject, body, smtp, portSmtp):

    """ Login to smtp and send email"""
    try: 
        smtpObj = smtplib.SMTP(smtp, portSmtp)
        smtpObj.ehlo()
        smtpObj.starttls()
    except:
        menssage = 'SMTP or Port error. Check your information. '
        menssage += 'You can modify your mail, with "-c -edit"'
        print (menssage)
    else:
        try: 
            smtpObj.login(myEmail, password)
        except smtplib.SMTPAuthenticationError: 
            menssage = 'Email adrress of password error. Check your information. '
            menssage += 'You can modify your mail, with "-c -edit"'
            print (menssage)
        else: 
            print ('Sending weather email to %s...' %to)
            smtpObj.sendmail(myEmail, to, 'Subject:'+subject +'\n'+ body)
            smtpObj.quit()
