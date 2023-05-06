import keys 
from twilio.rest import Client 

client= Client(keys.accountSID, keys.athToken) 

TwillioNumber= '+15077107744'
mycellphone= '8323169536' 

textmessage= client.messages.create(to=mycellphone, from_=TwillioNumber, body="Hey there!")




print(textmessage.status) 


call= client.calls.create(url= "http://demo.twilio.com/docs/voice.xml", to=mycellphone, from_=TwillioNumber) 
