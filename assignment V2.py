from twilio.rest import TwilioRestClient        #import twilio to enable calls
from twilio import twiml                        #import twiml to enable response use
import csv                                      #import csv module
import time                                     #import time module to use sleep function                        

csvFile = open('numbers.csv', "r")              #open csv file to read, set as variable for smaller coding
cr = csv.reader(csvFile, dialect='excel')       #set variable to function csv.reader which iterates through the csv row by row
number = []                                     #empty list for the numbers
name = []                                       #empty list for the name

for row in cr:                                  #cycle through the rows in the csv file
    number.append(row[0])                       #add the number value from the first field in the csv
    name.append(row[1])                         #add the name value from the second field to the list


account = "AC3f80902ce88436d89edb1112226c0298"  #Twilio account number
token = "c45c6fb7483cdbffeeaea8075310aa99"      #Twilio Token
client = TwilioRestClient(account, token)       #Variable to remember client details

count = 0                                       #Counter variable so code would work no matter the size of the csv
for record in number:                           #Cycle through each record in the list
    call = client.calls.create(to=str(number[count]), from_="441290211633", url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient") 
    print(call.sid)                             #Create a call above as part of client, use numbers from csv and my own trilio number as the from
    print("Calling", name[count])               #Print out the name of the user it is calling (pulled from the name list from the csv)
    time.sleep(5)
    count += 1                                  #Increment counter for sake of index values


### The below code is for using voice messages to respond to INCOMING calls ###
message = twiml.Response()                            #Use twiml to get a response to use say
message.say("Hello " + name[0], voice = twiml.Say.MAN, loop = 10)         #Say hello and concact the name of the current record
print(str(message))                         #Print it for callers reference
time.sleep(3)                               #Small time delay

