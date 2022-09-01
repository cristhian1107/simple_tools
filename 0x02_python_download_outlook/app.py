from pathlib import Path  # Core python module.
from engine.settings import Settings  # Environment Variables.
import win32com.client as win32  # pip install pywin32.

# Get path.
output_dir = Path(Settings.get_path())

# Connect to outlook.
outlook = win32.Dispatch('Outlook.Application').GetNamespace('MAPI')

# Connect to folder and get subfolder.
inbox = outlook.GetDefaultFolder(6)
sub_folder = inbox.Folders(Settings.get_subfolder())

# Loop messages.
for msg in sub_folder.Items:
    for attachment in msg.Attachments:
        path_file = Path(output_dir / str(attachment))
        attachment.SaveAsFile(output_dir / str(attachment))
