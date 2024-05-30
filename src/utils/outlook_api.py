import os
from lib.outlook_lib import outlook

# mail = outlook.Outlook()
# mail.login('smart_lead_bot@outlook.com', '#hwdmbf4kJ')
# mail.inbox()
# print(mail.unread())

for cp in os.environ.get("path").split(";"):
    print(cp)

