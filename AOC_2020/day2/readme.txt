

After your heroic deeds regaining control of the control centre yesterday, Elf McSkidy has decided to give you an important job to do.

"We know we've been hacked, so we need a way to protect ourselves! The dev team have set up a website for the elves to upload pictures of any suspicious people hanging around the factory, but we need to make sure it's secure before we add it to the public network. Please perform a security audit on the new server and make sure it's unhackable!"

You listen to the briefing and accept the task, pressing the deploy button to start the server as you do so.

McSkidy once again gives you a dossier of useful information to help you with your task, which you read as you wait for the server to boot:
Watch DarkStar's video on solving this task!

Dossier Compiled by @MuirlandOracle

﻿GET Parameters and URLs

We looked briefly at the differences between GET and POST requests in the previous dossier; however, the emphasis was on the POST requests used in a login form. The server you'll be testing today employs a concept called "GET parameters". Just as POST requests can be used to send information to the server, so too can GET requests be used; however, there is one important difference. With POST requests the data being sent is included in the "body" of the request. With GET requests, the data is included in the URL as a "parameter". This is best demonstrated with an example:

https://www.thebestfestivalcompany.co.uk/index.php?snack=mincePie](https://www.thebestfestivalcompany.co.uk/index.php?snack=mincePie

(Please Note: this site is completely fictitious. It does not exist, and connecting to it is not part of the task)

There are 7 different parts which make up this URL. Let's look at each of them in turn:


    First up we have the protocol (https://). This specifies whether the request should be made using HTTP, or HTTPS. In our example, we are using HTTPS.
    Next we have the subdomain (www). This is traditionally "www" (World Wide Web) to signify that the target is a website; however, this is not essential. Indeed, subdomains can be basically anything you want; for example, a lot of websites use things like "assets", or "api" to indiciate different subdomains with different uses. (e.g. https://api.thebestfestivalcompany.co.uk)
    The next part of the URL is the domain (thebestfestivalcompany). Domains need to be registered, and are used as links between a memorable word or phrase, and an IP address. In other words, they're used to give a name to the server running a website.
    Next up we have the TLD (Top Level Domain) -- .co.uk, for our example. Top level domains are used by DNS to determine where to look if they want to find your domain. Previously top level domains had specific uses (and many still do!), but this is not always the case these days. For example, .co.uk  indicates a company based in the UK, .com indicates a company based in the US.
    We then have the resource that we're selecting -- in this case that is the homepage of the website: index.php. As a side note, all homepages must be called "index" in order to be correctly served by the webserver without having to be specified fully. This is how you can go to https://tryhackme.com without having to specify that you want to receive the home page -- the index page is served automatically because you didn't specify!
    The final two aspects of the URL are the most important for our current topic: they both relate to GET parameters. First up we have ?snack=. Here ? is used to specify that a GET parameter is forthcoming. We then have the parameter name: snack. This is used to identify the parameter to the server. We then have an equals sign (=), indicating that the value will come next.
    Finally we have the value of the GET parameter: mincePie, because who doesn't like a mince pies, right?

It's important to note exactly which part of the URL is the GET parameter. Specifically, we are talking about ?snack=mincePie. If there was more than one parameter, we would separate them with an ampersand (&). For example: ?snack=mincePie&drink=hotChocolate. In this way we can send multiple values to the server, distinguished by keys (i.e. "mincePie" is identified by the key: "snack").

File Uploads

There are countless uses for file uploads in the modern internet -- profile pictures, school/university submissions, diagrams, pictures of your dog, you name it! Whilst file uploads are very common, they're also very easy to implement in an insecure fashion. For this reason, it's important that we understand the gravity of the attack vector.

When you have the ability to upload files to a server, you have a path straight to RCE (Remote Command Injection). An upload form with no restrictions would mean that you could upload a script that, when executed, connects back to your attacking machine and gives you the ability to run any command you want. It would be very unusual to find a file upload with no filtering; but it's much less uncommon to find a file upload that employs flawed filtering techniques which can be circumvented to upload a malicious script. The script has to be written in a language which the server can execute. PHP is usually a good choice for this, as most websites are still written with a PHP back end.

There isn't time to go over every kind of filter bypass in this task (there is literally an entire room on this topic, which is recommended for further practice). Instead we'll just cover one of the most common types of filter and its bypass:

    File Extension Filtering: As the name suggests extension filtering checks the file extension of uploaded files. This is often done by specifying a list of allowed extensions, then checking the uploaded file against the list. If the extension is not in the allowlist, the upload is rejected.
    So, what's the bypass? Well, the answer is that it depends entirely on how the filter is implemented. Many extension filters split a filename at the dot (.) and check what comes after it against the list. This makes it very easy to bypass by uploading a double-barrelled extension (e.g. .jpg.php). The filter splits at the dot(s), then checks what it thinks is the extension against the list. If jpg is an allowed extension then the upload will succeed and our malicious PHP script will be uploaded to the server.

When implementing an upload system, it's good practice to upload the files to a directory that can't be accessed remotely. Unfortunately, this is often not the case, and scripts are uploaded to a subdirectory on the webserver (often something like /uploads, /images, /media, or /resources). For example, we might be able to find out uploaded script at https://www.thebestfestivalcompany.co.uk/images/shell.jpg.php.

Reverse Shells

Let's assume that we've found somewhere to upload our malicious script, and we've bypassed the filter -- what then? There are a few paths we can take: the most common of which is uploading a reverse shell. This is a script that creates a network connection from the server, to our attacking machine. The majority of webservers are written with a PHP back end, which means we need a PHP reverse shell script -- there happens to be one already on Kali/AttackBox at /usr/share/webshells/php/php-reverse-shell.php (Note: if you're not using Kali or the provided AttackBox, the same script can be found here).

    Copy the webshell out into your current directory (cp /usr/share/webshells/php/php-reverse-shell.php .), then open it with your text editor of choice.
    Scroll down to where it has $ip and $port (both marked with // CHANGE THIS). Set the IP to your TryHackMe IP Address (which can be found in the green bubble on the navbar, if you're using the AttackBox, or by running ip a show tun0 if you're using your own Linux VM with the OpenVPN connection pack) -- making sure to keep the double quotes. Set the port to 443 with no double quotes, then save and exit the fiole. Congratulations, you now have a fully configured PHP reverse shell script!

PHP reverse shells can be very easily activated when stored in an accessible location: simply navigate to the file in your browser to execute the script (and send the reverse shell):

In the diagram, we first upload our shell. We then navigate to it in our browser, causing the server to send a reverse shell back to our waiting listener.
For a more in-depth explanation of reverse shells, check out the Intro to Shells room.

Reverse Shell Listeners


We've spoken at length about reverse shell listeners, but what are they? In short, a reverse shell listener is used to open a network socket to receive a raw connection -- like the one created by a reverse shell being executed! The simplest form of listener is created by using a program called netcat, which is installed on both Kali and the AttackBox by default. We can create a listener for an uploaded reverse shell by using this command: sudo nc -lvnp 443. This essentially creates a listener on port 443 (chosen as it's a port commonly left unfiltered by egress firewalls). Our reverse shell will be able to connect back to this when activated.

The full explanation can be found in the Intro to Shells room linked above, if you're interested.

Putting it all together

This was a lot of information, so let's put it all together and look at the full process for exploiting a file upload vulnerability in a PHP web application:

    Find a file upload point.
    Try uploading some innocent files -- what does it accept? (Images, text files, PDFs, etc)
    Find the directory containing your uploads.
    Try to bypass any filters and upload a reverse shell.
    Start a netcat listener to receive the shell
    Navigate to the shell in your browser and receive a connection!

At the bottom of the dossier is a stick note containing the following message:

    For Elf McEager:
    You have been assigned an ID number for your audit of the system: ODIzODI5MTNiYmYw . Use this to gain access to the upload section of the site.
    Good luck!

You note down the ID number and navigate to the displayed IP address in your browser.


------------------------------------------------------------------------------------------------


What string of text needs added to the URL to get access to the upload page?
'''
?id=ODIzODI5MTNiYmYw
'''


What type of file is accepted by the site?
'''
image
'''

Bypass the filter and upload a reverse shell.
In which directory are the uploaded files stored?
'''
/uploads/
'''


Activate your reverse shell and catch it in a netcat listener!
'''
no answer
'''


What is the flag in /var/www/flag.txt?
'''
THM{MGU3Y2UyMGUwNjExYTY4NTAxOWJhMzhh}
'''


