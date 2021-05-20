# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
#account_sid = os.environ['TWILIO_ACCOUNT_SID']
#auth_token = os.environ['TWILIO_AUTH_TOKEN']
account_sid = 'AC87ab611d9c527618e724cf1427fef9b7'
auth_token = 'dc06d92b638e231c5cce9f4dba43d53b'
client = Client(account_sid, auth_token)

calls = client.calls.list(limit=20)

for record in calls:
    print(record.id)
