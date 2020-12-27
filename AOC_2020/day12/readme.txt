 Day 12: Ready, set, elf. - Prelude:

Christmas is fast approaching, yet, all remain silent at The Best Festival Company (TBFC). What gives?! The cheek of those elves - slacking at the festive period! Santa has no time for slackers in his workshop. After all, the sleigh won't fill itself, nor will the good and naughty lists be sorted. Santa has tasked you, Elf McEager, with whacking those elves back in line.

12.1. Getting Started:
Before we begin, we're going to need to deploy two Instances:

    The THM AttackBox by pressing the " Start AttackBox" button at the top-right of the page.
     The vulnerable Instance attached to this task by pressing the "Deploy" button at the top-right of this task/day

12.2. Todays Learning Objectives:

We're going to be applying some of the skills and techniques we previously explored in this year's Advent of Cyber. Let's put on our enumeration caps, crack our knuckles and get hands-on with learning about, discovering and exploiting an interesting functionality of web servers.

Made with ❤ by CMNatic


12.3. Vulnerability...reveal yourself!
As an application's lifecycle continues, so does its version numbering. Applications contain seemingly innocent hallmarks of information such as version numbering. Known as information disclosure, these nuggets of information are handed to us by the server through error messages such as in the following screenshot, HTTP headers or even on the website itself.

An attacker can use knowledgebases such as Rapid7, AttackerKB, MITRE or Exploit-DB to look for vulnerabilities associated with the version number of that application. Vulnerabilities are attributed by a CVE number. You can learn more about these in MuirlandOracle's Intro to Research room.



12.4. Everything CGI (And no, not the movie kind...)
As you may have discovered throughout the "Web" portion of the event, webservers don't just display websites...They are capable of interacting with the operating system directly. The Common Gateway Interface or CGI for short is a standard means of communicating and processing data between a client such as a web browser to a web server.

Simply, this technology facilitates interaction with programmes such as Python script files, C++ and Java application, or system commands all within the browser - as if you were executing it on the command line.


(America Online., 1999)

Despite their age, CGI scripts are still relied upon from devices such as embedded computers to IoT devices, Routers, and the likes, who can't run complex frameworks like PHP or Node.


12.5. The Nitty Gritty
Whilst CGI has the right intentions and use cases, this technology can quickly be abused by people like us! The commonplace for CGI scripts to be stored is within the /cgi-bin/ folder on a webserver. Take, for example, this systeminfo.sh file that displays the date, time and the user the webserver is running as:

When navigating to the location of this script using our browser, the script is executed on the web server, the resulting output of this is then displayed to us. How could we use this?

12.6. As We've Demonstrated...
We could, perhaps, parse our own commands through to this script that will be executed. Because we know that this is a Ubuntu machine,  we can try some Linux commands like ls to list the contents of the working directory:


Or on a Windows machine, the systeminfo command reveals some useful information:

This is achieved by parsing the command as an argument with ?& i.e. ?&ls. As this is a web server, any spaces or special characters will need to be URL encoded.

12.7. There are tools for this! Practical Metasploit
Now we understand the application that's running, tools such as Metasploit can be used to confirm suspicions and hopefully leverage them! After some independent research, this application is vulnerable to the ShellShock attack (CVE 2014-6271)

Let's start Metasploit's console and use the ShellShock payload. (TryHackMe's room and blog post on Metasploit will be useful here)

At the minimum, when using an exploit, Metasploit needs to know two things:

    Your machine (such as the TryHackMe AttackBox) that you're attacking from (LHOST)
    The target that you're attacking (RHOST(S))

Exploits will have their own individual settings that you will need to configure. We can list these by using the options command, then using set OPTION VALUE accordingly. In our example, the exploit involves CGI scripts and as such, we must specify the location of the script on the webserver that we're attacking. In the example so far, this was at http://10.0.0.1/cgi-bin/systeminfo.sh

In order for the attack used as the example in this task to work, the options would be set like so:

    LHOST - 10.0.0.10 (our PC)
    RHOST - 10.0.0.1 (the remote PC)
    TARGETURI /cgi-bin/systeminfo.sh (the location of the script)


Please note that these options are for the exploit used as an example, you will have to set these values accordingly for the challenge.

After ensuring our options are set right, Let's run the exploit to get a Meterpreter connection...Success!

To run system commands on the host, we will use shell. By creating a shell on the remote host, we can run system commands as if it were our own PC.

I highly recommend the RP: Metasploit room if you wish to delve into this wonderful framework further. 

12.8. It's Challenge Time
To solve Elf McSkidy's problem with the elves slacking in the workshop, he has created the CGI script: elfwhacker.bat

Deploy the instance attached to this task, use your NMAP skills from "Day 8 - What's Under the Christmas Tree?  to find out what port the webserver (MACHINE_IP) is running on...Visit the application and discover the installation version, weaponise this information by searching knowledgebases for exploits and Meterpreter payloads possible and whack those elves!.


As this is a Windows machine, please allow a minimum of five minutes for it to deploy before beginning your enumeration.


Bonus: There are at least two ways of escalating your privileges after you gain entry. Find these out and pivot at your leisure! (please note that this is optional for the day should you fancy the challenge...)

12.9. Where to go from here
DarkStar7471's  AttackerKB Room

Heavenraiza's MITRE room

DarkStar7471's RP:Metasploit Room



----------------------------------------------------------------------------



What is the version number of the web server?
'''
9.0.17
'''


What CVE can be used to create a Meterpreter entry onto the machine? (Format: CVE-XXXX-XXXX)
'''
CVE-2019-0232
'''


Set your Metasploit settings appropriately and gain a foothold onto the deployed machine.
'''
no answer
'''


What are the contents of flag1.txt
'''
thm{whacking_all_the_elves}
'''


Looking for a challenge? Try to find out some of the vulnerabilities present to escalate your privileges!
'''
no answer
'''

