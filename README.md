# SlackMessageSender

Python script that sends a message to a channel within a Slack chat using the Slack API. Must include a valid API token
in line 10 for it to function.

#Instructions
Must have python installed.
Requires three command line arguments:

1. `-c` if your are sending the message to public channel, `-g` if you are sending to private channel

2. The name of the channel

3. The message with '+' signs to instead of spaces.

Ex. So if you wanted to send "Hello, my name is Joe" to a public channel called "friends" you would write this:
`python slack_message_sender_prod.py -c friends Hello+my+name+is+Joe`


