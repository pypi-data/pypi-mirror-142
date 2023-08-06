# Outlook Email Dispatcher

### A Simple Email Dispatcher based on top of win32Api

## Example of Usage: 


### Create a new Mail

CC and Attachments are Optional

```
FILES_TO_ATTACH_FOLDER = os.path.join(os.getcwd(), 'files_to_attach')
ATTACHMENTS = [os.path.join(FILES_TO_ATTACH_FOLDER, f) for f in os.listdir(FILES_TO_ATTACH_FOLDER)]

mail = Mail(
     Subject="Your Subject Here",
    To="example@example.com",
    HTMLBody="<h1>Your message Here</h1>",
    CC="example@example.com",
    Attachments=ATTACHMENTS,
)
```

### Initialize Outlook

Instanciate an Object from Outlook Class


```
outlook = Outlook()
```

### Preview Mail:
```
outlook.preview(mail)
```

### Send Mail:
```
outlook.send(mail)
```


