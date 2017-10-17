import json
import requests
import smtplib
from twilio.rest import TwilioRestClient



def sms(message):
    """ Signed up a free trial on twilio.com to send sms from a local number(twilio generated) to a verified phone number """

    print sms.__doc__
    account_sid = "ACc42f761c2a9fae0a93d32cf7e75d01b9"
    auth_token  = "19c962da002fc9157461561f5379f721"
    client = TwilioRestClient(account_sid, auth_token)
    print message
    #msg = client.messages.create(from_ = "(510) 901-5365", to = "(408) 637-1665", body=message )
    #print (message.sid)

def get_travel_duration():
    """ request google URL: (example)
    https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=Washington,DC&destinations=New+York+City,NY&key=AIzaSyCvjFtdl2WUe1s7I8yudl2ow7qegfIgsMg
    and use json to unpack the values and get the travel duration between a source and destination at the requested time"""

    print get_travel_duration.__doc__
    #response = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=Washington,DC&destinations=New+York+City,NY&key=AIzaSyCvjFtdl2WUe1s7I8yudl2ow7qegfIgsMg")
    response = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=1730+North+1st+Street,+San+Jose,+CA&destinations=Olive+West+Apartments,+1229+Vicente+Dr,+Sunnyvale,+CA+94086&key=AIzaSyCvjFtdl2WUe1s7I8yudl2ow7qegfIgsMg")

    #Sample result of google distance matrix api result
    """// 20170920230644
    // https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=1730+North+1st+Street,+San+Jose,+CA&destinations=Olive+West+Apartments,+1229+Vicente+Dr,+Sunnyvale,+CA+94086&key=AIzaSyCvjFtdl2WUe1s7I8yudl2ow7qegfIgsMg

    {
      "destination_addresses": [
        "1229 Vicente Dr, Sunnyvale, CA 94086, USA"
      ],
      "origin_addresses": [
        "1730 N 1st St, San Jose, CA 95112, USA"
      ],
      "rows": [
        {
          "elements": [
            {
              "distance": {
                "text": "11.1 mi",
                "value": 17933
              },
              "duration": {
                "text": "17 mins",
                "value": 992
              },
              "status": "OK"
            }
          ]
        }
      ],
      "status": "OK"
    }"""
    data = response.json()
    duration = [i['duration']['text'] for item in data['rows']  for i in item['elements']][0]
    dest_addr = data['destination_addresses'][0]
    origin_addr = data['origin_addresses'][0]
    print duration
    print 'from: ', dest_addr
    print 'to: ', origin_addr
    message = "Duration from '"+dest_addr+"' to '"+origin_addr+"' is '"+duration+"'"
    print message
    return message

def send_email():
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login('prethiguru@gmail.com', 'prethigwish')
    smtpObj.sendmail( '7328044372', '4086371665@att.net', 'hi' )

    print 'msg sent'

def main():
    """  Main func """

    print main.__doc__
    message = get_travel_duration()
    sms(message)

    #send_email()
    #sms()

if __name__ == '__main__':
    main()
