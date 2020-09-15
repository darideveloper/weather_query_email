#! python3
# Login to SMTP and send email

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendEmail (myEmail, password, to, subject, smtp, portSmtp, textAndHtml):

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
        
            # Create message container - the correct MIME type is multipart/alternative.
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = myEmail
            msg['To'] = to
            
            # Record the MIME types of both parts - text/plain and text/html.
            part1 = MIMEText(textAndHtml['text'], 'plain')
            part2 = MIMEText(textAndHtml['html'], 'html')

            # Attach parts into message container.
            msg.attach(part1)
            msg.attach(part2)

            # Send the message via local SMTP server.
            smtpObj.sendmail(myEmail, to, msg.as_string())
            smtpObj.quit()

def getTextAndHtml (infoWeather, todayWeather): 
    """ From infoWeather get text and html"""
    text = "Weather information... "
    table = ''

    # Count the days in the infoWeather
    days = []
    for hourWeather in infoWeather: 
        if hourWeather['day'] not in days: 
            days.append(hourWeather['day'])
    
    # Ganarate table
    for day in days: 
        table += """\
                <tr>
                    <th colspan="3"><h3> %s </h3></th>
                </tr>
                """ % (hourWeather['day'])
        for hourWeather in infoWeather: 
            if day == hourWeather['day']: 
                
                # Ganarate table
                table += """\
                <tr>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                </tr>
                """ % (str(hourWeather['hour'])+':00', hourWeather['main'], hourWeather['description'])

    # Ganerate table and add html
    html = """\
    <html>
        <head> 
            <style type="text/css">
                th {
                    text-align: center;
                    background-color: #ffffff;
                    color: #007b87
                }

                td {
                    text-align: center;
                }
                
                table {
                    width: 300px;
                    border-width: 0px;
                    border-style: none;
                    border-color: #e3e3d3;
                    padding: 0px;
                    border-spacing: 0px;
                }

                h1 {
                    color: #00444a
                }

                h2 {
                    color: #006973
                }
            </style>
        </head>
        <body>
            <p>
                <h1> Today Weather </h1>
                <h2> <b> %s </b></h2> 
                <h2> All weather information: </h2>
                <table>
                    %s
                </table>
            </p>
        </body>
    </html>
    """ % (todayWeather['text'], table)

    return {'text': text, 'html': html}

