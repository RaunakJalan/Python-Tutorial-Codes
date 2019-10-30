from twilio.rest import Client



account_sid = '<auth_id>' # Found on Twilio Console Dashboard

auth_token = '<auth_token>' # Found on Twilio Console Dashboard



myPhone = '<Phone number>' # Phone number you used to verify your Twilio account

TwilioNumber = '<Twilio_Number>' # Phone number given to you by Twilio



client = Client(account_sid, auth_token)



client.messages.create(

  to=myPhone,

  from_=TwilioNumber,

  body='I sent a text message from Python! ' + u'\U0001f680')
