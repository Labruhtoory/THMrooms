Introduction & Story:

We're going to be taking a look at some of the fundamental tools used in web application testing. You're going to learn how to use Gobuster to enumerate a web server for hidden files and folders to aid in the recovery of Elf's forums. Later on, you're going to be introduced to an important technique that is fuzzing, where you will have the opportunity to put theory into practice.

Our malicious, despicable, vile, cruel, contemptuous, evil hacker has defaced Elf's forums and completely removed the login page! However, we may still have access to the API. The sysadmin also told us that the API creates logs using dates with a format of YYYYMMDD.

What is Fuzzing?
To keep it simple, fuzzing can be argued as "fancy bruteforcing" to some degree. However, you can fuzz what you can't bruteforce. Fuzzing is using security tools to automate the input of data we provide into things such as websites or software applications. Fuzzing is an extremely effective process as computers can perform laborious actions like trying to find hidden files/folders, try different username and passwords much quicker then a human can (and is willing to do...)

Poorly built applications are often unable to handle data the way it is supposed to under intense load. Moreover, the data we're parsing to the application may be interpreted and executed (instead of being handled correctly i.e. system commands). We can use fuzzing to cause the application to trigger what's known as an error condition where this may be abused by a penetration tester or a bug bounty hunter.



An Introduction to Using Gobuster
Logically speaking, there are many pieces to a website that the average user doesn't see. They can be anything from a sitemap to a secret directory which contains important files. Unfortunately, this can cause developers to get a bit lazy, and not protect these directories, allowing anyone who finds out that they exist to steal the important data. gobuster is the tool that helps us discover these valuable directories if they exist. The idea behind the tool itself is simple, bruteforcing common paths to check if it's valid. Similar to how you would in your browser, albeit this tool is much, much quicker. Gobuster has three modes: dir, vhost and dns.

For the sake of today, we're going to be using gobuster in dir mode, as this is the most likely mode that you'll be using day-to-day. dir (short for directory) can be selected by using gobuster dir <rest of command>

Let's use the table below to illustrate how wordlists work:
Original URL 	Item in Wordlist 	Final URL
http://example.com 	backups 	http://example.com/backups
http://loveucmnatic.thm 	shepards 	http://loveucmnatic.thm/shepards



Gobuster has a few other little tricks, it supports appending extensions which means you can bruteforce files as well. We can use another handy little chart to visualize it and show an example later on:
Original URL 	Item in Wordlist 	Specified Extension 	Final URL
http://example.com 	backup 	php 	http://example.com/backup.php
http://example.com 	backup 	txt 	http://example.com/backup.txt
http://example.com 	icecream 	html 	http://example.com/icecream.html

To find the data in the table above, we have used a command such as the following (assuming wordlist.txt had the words "backup" and "icecream"): gobuster dir -u http://example.com -w wordlist.txt -x php,txt,html.

Whilst Gobuster is considerably faster than alternatives such as Dirbuster on Kali Linux, it is still limited to the wordlists and options that you provide. The more appropriate your wordlist is to the target, the better your results will be. Wordlists such as SecLists have wordlists for specific applications and platforms. You can use the information gathered from enumerating to help determine what wordlist may be the most appropriate to use. Although, we will come onto refining those skills in a later day.
seclists1

Gobuster itself works like any other Linux tool, meaning it has an online man page available here, which you can use as a reference if you want to learn more about the various options that gobuster supports. However, let's detail a few of the common options below:
Options 	Description
-u 	Used to specify which url to enumerate
-w 	Used to specify which wordlist that is appended on the url path i.e

"http://url.com/word1"

"http://url.com/word2"

"http://url.com/word3.php"
-x 	Used to specify file extensions i.e "php,txt,html"

Recommended wordlist﻿ to use: big.txt

We have provided wordlists for you on the AttackBox located in "/usr/share/wordlists". This is also the default location for wordlists on pentesting distributions such as Kali Linux. To provide an example, "big.txt" is located at the file path "/usr/share/wordlists/dirb/big.txt". Take some time to explore other wordlists provided and think of the situation where they may be effective to use.



An Introduction to Using wfuzz
The premise behind wfuzz is simple. Occasionally you want a bit more information about how much data something within a web application returns. This could be anything from a file, a response code (i.e. 404 meaning the URL doesn't exist) or the parameters used in a form similar to the form you attacked in Day 2.

For example, let's say you are pentesting a note-taking application and you want to see if you can view notes by other users. One way you may want to achieve this is by FUZZing for usernames (with the knowledge that every valid user will have note.txt by default). Our wfuzz command would like the following: wfuzz -c -z file,/usr/share/wordlists/dirb/big.txt localhost:80/FUZZ/note.txt

Now wfuzz will query the webserver using the words iterated from the "big.txt" wordlist. To illustrate:

    Query #1: http://localhost/admin/note.txt
    Query #2: http://localhost/administrator/note.txt
    Query #3: http://localhost/system/note.txt


Note how the "FUZZ" parameter is being replaced with the words from the wordlist. We'll outline some of the options that can be configured in wfuzz, however, it's worth knowing that will display results that are different to the parameters that we set. In the picture above we used the --hwoption to hide all pages that have 57 words on them. Since wfuzz found a URL with only 8 words, it'll be displayed to us, as this is not 57 words.

    It is important to know that you can FUZZ any part of the URL, meaning that you can test any parameters if you don't know them as well.

As with any Linux-based tool, wfuzz also has a useful manpage here, that details some of the more advanced options available to you. Although, I have added some of the more useful options into the table below:
Options 	Description
-c 	Shows the output in color
-d 	Specify the parameters you want to fuzz with, where the data is encoded for a HTML form
-z 	Specifies what will replace FUZZ in the request. For example -z file,big.txt. We're telling wfuzz to look for files by replacing "FUZZ" with the words within "big.txt"
--hc 	Don't show certain http response codes. I.e. Don't show 404 responses that indicate the file doesn't exist, or "200" to indicate the file does exist
--hl 	Don't show for a certain amount of lines in the response
--hh 	Don't show for a certain amount of words



Let's bring this together and demonstrate some of these options. Let's say we wanted to fuzz an application on http://shibes.thm/login.php to find the correct credentials to the login form. After recalling our knowledge from Day 2, we know all about URL parameters! We can take a bit of a guess as to what parameters the login form may be using username and password, right? Worth a try! Our wfuzz command would look like so: wfuzz -c -z file,mywordlist.txt -d “username=FUZZ&password=FUZZ” -u http://shibes.thm/login.php

Where wfuzz will now iterate through the wordlist we provided and replace the "FUZZ" values specified in the "username" and "password" parameters.



Challenge

Deploy both the instance attached to this task (the green deploy button) and the AttackBox by pressing the blue "Start AttackBox" button at the top of the page. After allowing 5 minutes, navigate to the website (MACHINE_IP) in your AttackBox browser.

It is up to you to decide if you wish to create the wordlist yourself or use a larger wordlist located in /opt/AoC-2020/Day-4/wordlist on the AttackBox. The wordlist is also available for download if you are using your own machine.

In summary, use the tools and techniques outlined in today's advent of cyber; search for the API, find the correct post and bring back Elf's forums!



How to approach the challenge

Since we know there's theoretically an API directory we can use gobuster to enumerate the website and see if we can find anything. Then assuming we do find something, we should investigate it for interesting files. Let's say we then find what seems to hold the logs, we know we're searching by date, so we can infer that there's a good chance that we'll be using the date parameter to interact with the API. We also know that the API takes a date in the form of YYYYMMDD. A wordlist in that format can be found in the hint for this task, although if you want an extra challenge, you can try and build a wordlist in that format yourself.

Finally, API's may not return data if the proper parameters aren't passed, so with that knowledge, we can use the options in wfuzz to filter out parameters that don't return anything.

With all that in mind, we should be able to get a flag.
Recommended Rooms:

TryHackMe | ZTH: Web 2

TryHackMe | CC: Pen Testing






------------------------------------------------------------------------------------------------


Deploy your AttackBox (the blue "Start AttackBox" button) and the tasks machine (green button on this task) if you haven't already. Once both have deployed, open FireFox on the AttackBox and copy/paste the machines IP (MACHINE_IP) into the browser search bar.
'''
no answer
'''


Given the URL "http://shibes.xyz/api.php", what would the entire wfuzz command look like to query the "breed" parameter using the wordlist "big.txt" (assume that "big.txt" is in your current directory)
'''
wfuzz -c -z file,big.txt http://shibes.xyz/api.php?breed=FUZZ
'''


Use GoBuster to find the API directory. What file is there?
'''
site-log.php
'''


Fuzz the date parameter on the file you found in the API directory. What is the flag displayed in the correct post?
'''
THM{D4t3_AP1}
'''

