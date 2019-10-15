from twilio.rest import Client



account_sid = 'AC372ba4054aeba0e57ab832ccc00fa0bf' # Found on Twilio Console Dashboard

auth_token = 'a1ddd43a44b336db7862f2bdda65c337' # Found on Twilio Console Dashboard



myPhone = '+917984590915' # Phone number you used to verify your Twilio account

TwilioNumber = '18594708166' # Phone number given to you by Twilio



client = Client(account_sid, auth_token)



client.messages.create(

  to=myPhone,

  from_=TwilioNumber,

  body='I sent a text message from Python! ' + u'\U0001f680')
