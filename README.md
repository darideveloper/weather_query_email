# weather_query_email
## Description
This is a terminal project.
**Get information of weather, by email**, connecting with the api **Open Weather.**
# How to use
## Api weather account
You need to **create a free account** in https://openweathermap.org/, to **get your api key.**
## Credentials
The first time that you run the program, it request your email acount: 
* **email:** your email acountconfigurated to use as SMTP server.
* **password:** it will only be stored locally
* **SMTP server:** No one can access your information
* **SMTP port**
* **Subject:** The subject in the emails

You can **check your SMTP port and server** depends on the mail service you use (gmail, outlook, yahoo, etc)
You can get more information about SMAP configuration, here: 
* [Microsoft post](https://support.microsoft.com/es-es/office/configuraci%c3%b3n-de-correo-electr%c3%b3nico-pop-e-imap-para-outlook-8361e398-8af4-4e97-b147-6c6c4ac95353?ui=es-es&rs=es-es&ad=es)

## CSV emails
After credentials, the program will request a list of names and emails destination. 

The information is saved in **emails.csv**. 
You can **delete the file** so that the system will request the emails again.
And you can also **manually edit** the file to add or delete information, respecting the format: 'email, name'"


## Terminal interfaz

You can run the program by terminal. 
Use '--help' for more information in any moment on other keywords:

```bash
$ python3 main.py --help        

#Run the main.py to request credentials 
#write '-l --cred' to see all credentials 
#write '-e --cred' to edit all credentials 
#You can delete the file 'emails.csv' so that the system will request the emails again.
#You can also manually edit the file to add or delete information, respecting the format: 'email, name'"

```
## Run the program
When the program has the credentials and the email destination, it will do the following: 

**1. Connect to OPEN WEATHER API to get weather information.** 
**2. Format weather information as html table.**
**3. Read the list of emails. **
**4. Send send a email for each one in the list.**
# Use example
## Credentials

Example of credentials request: 

```bash
$ myEmail (Your email adrees (example: myEmail@gmail.com)):
'myemail@gmail.com'

$ password (Password of your email (example: 'my secret password')): 
'the password of my email'

$ smtp (Your smtp server (example: smtp.gmail.com)): 
'emtp.gmail.com'

$ portSmtp (Your smtp port (example: 587)):
'587'

$ apiKey (Api key of oppen weather): 
'148200b8d1c12c3d891801dc21123456'

$ subject (The subject of the emails:
'Email of weather' 
```

## CSV emails

Example of emails request:

``` bash
$ Recipient 1 name:
'dari'

$ Recipient 1 email:
'hernandezdarifrancisco@gmail.com'

$ Other recipient (y/n)
'y'

$ Recipient 2 name:
'dari 2'

$ Recipient 2 email:
'darialternative@gmail.com'

$ Other recipient (y/n)
'n'

```

# Screenshot o0f email 
![received mail](https://github.com/DariHernandez/weather_query_email/blob/master/screenshots/ss1.jpg)
