# This skeleton is valid for both Python 2.7 and Python 3.
# You should be aware of your additional code for compatibility of the Python version of your choice.

from socket import *
import argparse as ap
import getpass as gp

#Get sender_email and recipient_email as arguments to the program
#parser = ap.ArgumentParser(description='A test SMTP client without authentication')
#parser.add_argument('-f', '--from', dest='fromMail', required=True, metavar='<sender_email>')
#parser.add_argument('-t', '--to', dest='toMail', required=True, metavar='<recipient_email>')
#If using the authentication of the SMTP server, also get a valid username (optional exercise)
#parser.add_argument('-u', '--username', dest='username', required=True, metavar='<username>')

#args = parser.parse_args()
fromMail = "erling@kul.no" #Sender's email address
toMail = "ingrid@nerd.co" #Recipient's email address
#username = args.username #SMTP username in case you are implementing the optional exercise

#If using the authentication of the SMTP server, ask for a valid password (optional exercise)
#password = gp.getpass(prompt='Password: ')

# Message to send
msg = "\r\n I love sausage"
endmsg = "\r\n.\r\n"

# Our mail server is smtp.stud.ntnu.no but it allows only authenticated communications. (optional exercise)
# mailserver = 'smtp.stud.ntnu.no'
# You can run a local simple SMTP server such as "Fake SMTP Server" and communicate with it without authentication.
mailserver = 'localhost'

# Create socket called clientSocket and establish a TCP connection
# (use the appropriate port) with mailserver
#Fill in start

clientSocket = socket(AF_INET, SOCK_STREAM)
PORT = 6969
TCP_IP = '129.241.206.191'
clientSocket.connect((mailserver,PORT))

#Fill in end

recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
	print '220 reply not received from server.'

# Send HELO command and print server response.
# Can use EHLO instead since HELO is obsolete, but the latter can still be used
heloCommand = 'EHLO Hey\r\n'
#clientSocket.send(heloCommand.encode()) #Python 3
clientSocket.send(heloCommand) #Python 2.7
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server.'

# Send MAIL FROM command and print server response.
clientSocket.send('MAIL FROM:erlingerkul@msn.com\r\n') #include \r\n to symbolize end of message
recv2 = clientSocket.recv(1024)
print recv2

# Send RCPT TO command and print server response.
clientSocket.send('RCPT TO:ingrid@nerd.dk\r\n')
recv2 = clientSocket.recv(1024)
print recv2

# Send DATA command and print server response.
clientSocket.send('DATA\r\n')
rcv2 = clientSocket.recv(1024)
print recv2

# Send message data.
clientSocket.send(msg)
clientSocket.send(endmsg)
recv2 = clientSocket.recv(1024)
print recv



# Send QUIT command and get server response.
clientSocket.send('QUIT\r\n')
recv2 = clientSocket.recv(1024)
print recv2


#Note that there are more communications if you implement the optional exercise.
