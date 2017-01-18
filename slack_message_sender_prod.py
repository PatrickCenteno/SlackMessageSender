import requests
import json
import sys
import urllib

#constants for API calls
MESSAGE_URL = "https://slack.com/api/chat.postMessage"
GROUP_LIST_URL = "https://slack.com/api/groups.list"
CHANNEL_LIST_URL = "https://slack.com/api/channels.list"
TOKEN = "*** OMMITED FOR SECURITY ***"
AT_SIGN = "%40"

#will obtain these from command line
# channel_id = "G1DQX9CER"
# text = "%40vragosta%20%2D%2D"
# user = "%40pcenteno"

def main():
	# gets channel name text and user and whether or not is a public or private channel
	#from command line arguments
	if len(sys.argv) < 4:
		print "Invalid input"
		sys.exit()

	# Find id based public or private
	if sys.argv[1] == "-c":
		channel_id = find_public_channel(sys.argv[2])
	elif sys.argv[1] == "-g":
		channel_id = find_private_channel(sys.argv[2])
	else:
		print "Invalid input"
		sys.exit()

	text = sys.argv[3]

	send_message(channel_id, text)

''' Makes api call to find list of private channels
	if name exists, it returns the id '''
def find_private_channel(channel_name):
	api_call = GROUP_LIST_URL + "?token=" + TOKEN + "&" + "pretty=1"
	r = requests.get(api_call)
	group_response = json.loads(r.text)
	for g in group_response['groups']:
		if g['name'] == channel_name:
			return g['id']
	print "Channel doesnt exist"
	sys.exit()

''' Makes api call to find the list of public channels
	if name exists, it returns the id '''
def find_public_channel(channel_name):
	api_call = CHANNEL_LIST_URL + "?token=" + TOKEN + "&pretty=1"
	r = requests.get(api_call)
	channel_response = json.loads(r.text)
	for c in channel_response['channels']:
		if c['name'] == channel_name:
			return c['id']
	print "Channel doesnt exist"
	sys.exit()

''' Based on user input, send messages to the channel
	through slack API '''
def send_message(channel_id, text):
	safe_text = urllib.quote(text, '+')
	api_call = MESSAGE_URL + "?token=" + TOKEN + "&channel=" + channel_id + "&text=" + safe_text + "&as_user=true&pretty=1"
	r = requests.get(api_call)
	message_response = json.loads(r.text)
	if message_response['ok'] == True:
		print "You have sent the message"
	else:
		print "Error: message not sent"


if __name__ == '__main__':
	main()

