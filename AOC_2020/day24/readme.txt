It was the night before Christmas and The Best Festival Company could finally rest. All of the toys had been made and the company had recovered from attack after attack. Everything was in Santa's hands now, leaving the elves to do little more than wish him a safe journey ahead. Elf McEager sat at his terminal staring absentmindedly at light snow that had begun to fall. Just as he had drifted off to sleep Elf McEager was jolted to attention as a small parcel appeared just at the edge of his view. 

The present was wrapped in a deep blue velvet that appeared to shimmer in and out of the firelight, not unlike a blinking terminal prompt. Carefully, Elf McEager reached for the azure ribbon, untying it slowly so as to not damage it. The velvet slowly fell away, revealing a small NUC computer with a letter on top. Unfolding the letter, Elf McEager read it aloud:


"Elf McEager - your boundless effort to save Christmas this year has not gone unnoticed. I wanted to reward you with a special present, however, there's a catch. Elf McSkidy and I have seen your skills advance and we feel it would only be appropriate to give you a present after one last challenge. Inside this package, you'll have also found a computer. Plug this into the network and hack into it. Best of luck and Merry Christmas - Santa"


Without delay, Elf McEager connected the NUC appropriately and watched it whir to life. A small screen nearby the power button blinked and then displayed the IP address assigned to the device. Next to the IP, a small symbol appeared. McEager quietly wondered to himself what it could mean as he logged into his terminal, ready to start his final challenge. 




Wanting to follow along without it feeling so challenging? Watch one of the creators, Darkstar's video on solving today's challenge. 


Today's task is an accumulation of the skills you've gained throughout the Advent of Cyber 2. A dossier has been provided on various topics below as well which will aid in your journey. Don't be afraid to ask for help in the advent-of-cyber-2 Discord channel where necessary, just be sure to try your best! 


Client-Side Filters:

Way back in Day 2 we looked at how to bypass a server-side filter around a file-upload function. It's now time to see how to bypass a client-side filter.

In many ways, client-side filters are easier to bypass than their server-side equivalents as they execute on your own attacking computer -- putting them under the control of an attacker. For this reason, client-side filters should never be used as the sole security measure for the file upload functionality on a website.

So, how would we bypass a client-side filter? The easiest way is by using BurpSuite to intercept the JavaScript code file containing the filter before it ever actually reaches our browser, then either drop the file entirely or remove the filter from the code.

Opening a new BurpSuite project, the first thing we have to do is navigate to the "Proxy" tab, then the "Options" subsection:

By default BurpSuite does not intercept JavaScript files when proxying traffic, so we need to enable this feature before we can start deleting any client-side filters. To do this, we navigate to the "Intercept Client Requests" section, click on the top line (highlighted below), then click edit:

This will give us the option to edit the condition. Find and remove the |^js$ in the condition, then save the filter:

Next, go to the "Intercept Server Responses" section and select the "Intercept responses based on the following rules" checkbox:

This will now intercept all responses from the server, including the JavaScript files!

Now you can reload the upload page by pressing Ctrl + F5 (Note that this must be done with a hard refresh to prevent 304 Not Modified responses), proxying through BurpSuite. Keep an eye on the responses as they come back -- if one is called filter.js, it would probably be a good idea to drop it!

If you use Mac, the equivalent sequence for a hard refresh is Preferences -> Clear History, then Control + R.

For more information on this topic, see the Upload Vulnerabilities room!



Shell Upgrading and Stabilization:

You will be familiar with reverse shells from previous tasks or rooms; however, the shells you have been taught so far have had several fatal flaws. For example, pressing Ctrl + C killed the shell entirely. You could not use the arrow keys to see your shell history, and TAB autocompletes didn’t work. Stabilizing shells is an important skill to learn as it fixes all of these problems, providing a much nicer working environment.

Working inside the reverse shell:

    The first thing to do is use python3 -c 'import pty;pty.spawn("/bin/bash")', which uses Python to spawn a better-featured bash shell. At this point, our shell will look a bit prettier, but we still won’t be able to use tab autocomplete or the arrow keys, and Ctrl + C will still kill the shell.
    Step two is: export TERM=xterm – this will give us access to term commands such as clear.
    Finally (and most importantly) we will background the shell using Ctrl + Z. Back in our own terminal we use stty raw -echo; fg. This does two things: first, it turns off our own terminal echo (which gives us access to tab autocompletes, the arrow keys, and Ctrl + C to kill processes). It then foregrounds the shell, thus completing the process.

The full technique can be seen here:


Note that if the shell dies, any input in your own terminal will not be visible (as a result of having disabled terminal echo). To fix this, type reset and press enter.

See the Intro to Shells room for more information on this topic!



Your New Best Friend - The MySQL Client:

Databases are used by virtually every web application on the planet to some extent or another. For this reason it’s important that we know how to access them manually. One of the most common database servers available is MySQL (or its free fork: MariaDB, which uses identical syntax and is accessed in exactly the same way). This can be accessed manually using the mysql client. There’s a catch though – exposing a database publicly is a very bad idea, so, whilst it is possible to connect to a database remotely from your attacking machine using the MySQL client, we will be focussing on connecting to a database running locally.

To access a database using the MySQL client, we would use the following syntax:
mysql -uUSERNAME -p
This tells the client to connect to the local database using a username of USERNAME (Note the lack of space between the switch -u and the value!), using a password which it will ask us to enter when we run the command.

Having entered the password, we will be confronted with a prompt which looks something like this:

Note that this will look slightly different depending on whether it’s a MySQL server or a MariaDB server.

The next thing we should do is use the show databases; command to see the databases available:

In this screenshot, the top three databases are default for a MySQL/MariaDB installation. Any others are not.

Let’s take a look at the top_secret database.
To enter the database we use the use DATABASE; command, where DATABASE is the name of the target DB. We can then show all the tables in the database with show tables;:

In this screenshot there is only one table: users.

Let’s dump the users table. To do this we use the SQL command: SELECT * FROM users;.

We now have a username and a password we can look at cracking!



Online Password Cracking:

In the modern age of password cracking, weak passwords can often be cracked without any cracking at all! Many websites now exist with the sole goal of hosting rainbow tables - tables of previously cracked passwords. This allows us more than often to simply input a password hash and nearly instantly receive the cracked password. Some various sites that I find myself (Dark) commonly using, especially throughout the case of CTFs, include the following:

- https://crackstation.net/ 

- https://md5decrypt.net/en/ 

- https://hashes.com/en/decrypt/hash 


The landing page of crackstation.net



Privilege Escalation with LXD:

Among the more curious privilege escalation methods on Linux, lxd is certainly a mind-bender, to say the least. This technique involves leveraging a flaw in lxd, a program that we can use to spin up containers much akin to Docker. This exploit specifically involves abusing mount points to mount volumes from our victim machine (the machine we're attacking) within a container that we shouldn't be able to access/read. However, we have root powers on lxd containers - thus allowing us to bypass the read permission checks and escalate our privileges. We can perform this privesc method via the following steps:

1. First, we need to check and see if our user is a member of the lxd group. We can do this with the command: id



We can see in this case that the user is a member of the lxd group. Note, images from this section are from the source linked at the end with regards to additional information. 


2. Typically, this privesc can be a bit of a drawn-out process, however, in our case, we'll be able to skip part of the way through. To perform it properly, we have to perform the following steps.:

- Steps to be performed on the attacking machine:

- - Download build-alpine on your local machine via the git repository

- - Execute the script "build -alpine" that will build the latest Alpine image as a compressed file. This must be executed by the root user.

- - Transfer this newly created tar file to the victim machine


- Steps to be performed on the victim machine:

- - Download the alpine image

- - Import image for lxd

- - Initialize the image inside a new container <- Worth checking the already imported/available images as you may be able to skip to this step

- - Mount the container inside the /root directory


3. For the sake of this example, we'll be skipping close to the end (see the bolded bit above) by checking what images are readily available on the machine in question. We can do that via the following command: lxc image list



Checking what images are available via the command: lxc image list

4. Now for the fun bit. Next, we'll run a series of commands which initialize, configure the disks, and start the container. Image name needs to match up with the imported image we'll be using. In the case of the image above, that'd be the myimage alias previously assigned to it. The container name and device name are whatever your heart desires. In my example, I'm naming my container strongbad and the device trogdor.


lxc init IMAGENAME CONTAINERNAME -c security.privileged=true

Ex: lxc init myimage strongbad -c security.privileged=true


lxc config device add CONTAINERNAME DEVICENAME disk source=/ path=/mnt/root recursive=true

Ex: lxc config device add strongbad trogdor disk source=/ path=/mnt/root recursive=true


lxc start CONTAINERNAME

Ex: lxc start strongbad


lxc exec CONTAINERNAME /bin/sh

Ex: lxc exec strongbad /bin/sh


We'll then run just a few more commands to mount our storage and verify we've escalated to root:

id

cd /mnt/root/root


And that's it! If that was a bit of a mind-bender, I highly recommend checking out the resource provided below. 


Additional information on this privesc technique can be found here: Link


Credits: This room was created as a collaboration between Dark, Muiri, Varg, and Spooky


Remember that machines can take up to five minutes to boot up fully!




--------------------------------------------------------------------------
Scan the machine. What ports are open?
'''
80, 65000
'''


What's the title of the hidden website? It's worthwhile looking recursively at all websites on the box for this step. 
'''
Light Cycle
'''


What is the name of the hidden php page?
'''
uploads.php
'''


What is the name of the hidden directory where file uploads are saved?
'''
grid
'''


Bypass the filters. Upload and execute a reverse shell. 
'''
no answer
'''


What is the value of the web.txt flag?
'''
THM{ENTER_THE_GRID}
'''


Upgrade and stabilize your shell. 
'''
no answer
'''


Review the configuration files for the webserver to find some useful loot in the form of credentials. What credentials do you find? username:password
'''
tron:IFightForTheUsers
'''


Access the database and discover the encrypted credentials. What is the name of the database you find these in?
'''
tron
'''


Crack the password. What is it?
'''
@computer@
'''


Use su to login to the newly discovered user by exploiting password reuse. 
'''
no answer
'''


What is the value of the user.txt flag?
'''
THM{IDENTITY_DISC_RECOGNISED}
'''


Check the user's groups. Which group can be leveraged to escalate privileges? 
'''
lxc
'''


Abuse this group to escalate privileges to root.
'''
no answer
'''


What is the value of the root.txt flag?
'''
THM{FLYNN_LIVES}
'''