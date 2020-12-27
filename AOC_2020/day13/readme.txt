Day 13: Coal For Christmas
Prove these sysadmins deserve coal for Christmas!

Watch JohnHammond's video on solving this task!

Hi Santa, hop in your sleigh and deploy this machine!
'''
no answer 
'''

The Christmas GPS now says this house is at the address MACHINE_IP. Scan this machine with a port-scanning tool of your choice.

Port Scanning

We will begin by scanning the machine. If you are working from the TryHackMe "Attackbox" or from a Kali Linux instance (or honestly, any Linux distribution where you have this installed), you can use nmap with syntax like so:

nmap MACHINE_IP
'''
no answer
'''



What old, deprecated protocol and service is running?
'''
telnet
'''

Initial Access

Connect to this service to see if you can make use of it. You can connect to the service with the standard command-line client, named after the name of the service, or netcat with syntax like this:

telnet MACHINE_IP <PORT_FROM_NMAP_SCAN>

What credential was left for you?
'''
clauschristmas
'''


Enumeration

Looks like you can slide right down the chimney! Log in and take a look around, enumerate a bit. You can view files and folders in the current directory with ls, change directories with cd and view the contents of files with cat.

Often to enumerate you want to look at pertinent system information, like the version of the operating system or other release information. You can view some information with commands like this:

cat /etc/*release

uname -a 

cat /etc/issue 

There is a great list of commands you can run for enumeration here: https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/

What distribution of Linux and version number is this server running?
'''
Ubuntu 12.04
'''



This is a very old version of Linux! This may be vulnerable to some kernel exploits, that we could use to escalate our privileges.

Take a look at the cookies and milk that the server owners left for you. You can do this with the cat command as mentioned earlier.

cat cookies_and_milk.txt

Who got here first?
'''
Grinch
'''



The perpetrator took half of the cookies and milk! Weirdly enough, that file looks like C code...

That C source code is a portion of a kernel exploit called DirtyCow. Dirty COW (CVE-2016-5195) is a privilege escalation vulnerability in the Linux Kernel, taking advantage of a race condition that was found in the way the Linux kernel's memory subsystem handled the copy-on-write (COW) breakage of private read-only memory mappings. An unprivileged local user could use this flaw to gain write access to otherwise read-only memory mappings and thus increase their privileges on the system.

You can learn more about the DirtyCow exploit online here: https://dirtycow.ninja/

This cookies_and_milk.txt file looks like a modified rendition of a DirtyCow exploit, usually written in C. Find a copy of that original file online, and get it on the target box. You can do this with some simple file transfer methods like netcat, or spinning up a quick Python HTTP server... or you can simply copy-and-paste it into a text editor on the box!
'''
no answer
'''


You can compile the C source code on the target with gcc. You might need to supply specific parameters or arguments to include different libraries, but thankfully, the DirtyCow source code will explain what syntax to use.

What is the verbatim syntax you can use to compile, taken from the real C source code comments?
'''
gcc -pthread dirty.c -o dirty -lcrypt
'''


Privilege Escalation

Run the commands to compile the exploit, and run it.

What "new" username was created, with the default operations of the real C source code?
'''
firefart
'''


Switch your user into that new user account, and hop over to the /root directory to own this server!

You can switch user accounts like so:

su <user_to_change_to>
'''
no answer
'''


Uh oh, looks like that perpetrator left a message! Follow his instructions to prove you really did leave Coal for Christmas!

After you leave behind the coal, you can run tree | md5sum

What is the MD5 hash output?
'''
8b16f00dd3b51efadb02c1df7f8427cc
'''