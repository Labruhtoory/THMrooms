					[Task 1] Deploy the machine

#1 	

Deploy the machine
'''
no answer
'''

					[Task 2] Reconnaissance

#1 	

Scan this box
'''
no answer
'''

#2 	

Scan the box, how many ports are open?
'''
6
'''


#3 	

What version of the squid proxy is running on the machine?
'''
3.5.12
'''

#4 	

How many ports will nmap scan if the flag -p-400 was used?
'''
400
'''

#5 	

Using the nmap flag -n what will it not resolve?
'''
DNS
'''

#6 	

What is the most likely operating system this machine is running?
'''
ubuntu
'''

#7 	

What port is the web server running on?
'''
3333
'''

#8 	

Its important to ensure you are always doing your reconnaissance thoroughly before progressing. Knowing all open services (which can all be points of exploitation) is very important, don't forget that ports on a higher range might be open so always scan ports after 1000 (even if you leave scanning in the background)
'''
no answer
'''

					[Task 3] Locating directories using GoBuster

#1 	

Lets first start of by scanning the website to find any hidden directories. To do this, we're going to use GoBuster.
'''
no answer
'''

#2 	

What is the directory that has an upload form page?
'''
/internal/
'''

					[Task 4] Compromise the webserver 

#1 	Try upload a few file types to the server, what common extension seems to be blocked?
'''
.php
'''

#2 	

To identify which extensions are not blocked, we're going to fuzz the upload form.
'''
no answer
'''

#3 	

We're going to use Intruder (used for automating customised attacks).
'''
.phtml
'''

#4 	

Now we know what extension we can use for our payload we can progress.
'''
no answer
'''

#5 	

What is the name of the user who manages the webserver?
'''
bill
'''
	
#6 	

What is the user flag?
'''
8bd7992fbe8a6ad22a63361004cfcedb
'''

					[Task 5] Privilege Escalation 

#1

On the system, search for all SUID files. What file stands out?
'''
/bin/systemctl
'''

#2

Become root and get the last flag (/root/root.txt)
'''
a58ff8579f0a9270368d33a9966c7fd5
'''