# Pages
* [List ID Folder Outlook](https://docs.microsoft.com/en-us/office/vba/api/outlook.oldefaultfolders)

# Code
```python
# Get current path and create directory.
output_dir = Path.cwd() / 'attached'
output_dir.mkdir(parents=True, exist_ok=True)

# Select folder by ID List Inbox => 6.
inbox = outlook.GetDefaultFolder(6)

# Get subfolders.
inbox = outlook.GetDefaultFolder(6)
inbox.Folders

# Attributes for messages.
for eachFile in msgList:
    filePath = outDir + "\\" + eachFile
    msg = outlook.OpenSharedItem(filePath)
    print msg.ReceivedTime
    print msg.Subject
    print msg.Body
    print msg.To
    print msg.Size
    print msg.Attachments
```