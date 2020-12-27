Day 8: What's Under the Christmas Tree? - Story:

After a few months of probation, intern Elf McEager has passed with glowing feedback from Elf McSkidy. During the meeting, Elf McEager asked for more access to The Best Festival Company's (TBFC'z) internal network as he wishes to know more about the systems he has sworn to protect.

Elf McSkidy was reluctant to agree. However, after Elf McEager's heroic actions in recovering christmas, Elf McSkidy soon thought this was a good idea. This was uncharted territory for Elf McEager - he had no idea how to begin finding out this information for his new responsibilites. Thankfully, TBFC has a wonderful up-skill program covering the use of Nmap for ElfMcEager to enrol in.
8.1. Getting Started:

Before we begin, we're going to need to deploy two Instances:

    The THM AttackBox by pressing the "Start AttackBox" button at the top-right of the page.
    The vulnerable Instance attached to this task by pressing the "Deploy" button at the top-right of this task/day

8.2. Today's Learning Objectives:

We're going to be exploring the use of Nmap in our information gathering stage to build a picture of the services running on a remote computer, and to understand how these may be useful to use. We'll also be showing how Nmap scans can be detected and blocked by the use of firewalls.

Made with ❤ by CMNatic
8.3. Intro to Nmap:

An open-source, extensible, and importantly free tool, Nmap is one of the industry standard's that everyone should have in their toolkit. Nmap is capable of a few things that are essential in the Information Gathering stages of a penetration testing methodology such as the Penetration Testing Execution Standard (PTES), including:

    Host discovery
    Vulnerability discovery
    Service/Application discovery

8.4. Basic Nmap Functionality

We'll quickly gaze over the basics” of getting started with Nmap, the scan types, and the syntax for these types accordingly. We'll apply our networking knowledge learned yesterday in "Day 7 - The Grinch Really Did Steal Christmas" to help understand the differences between TCP and UDP scanning.

8.4.1 TCP Scanning

There are two common TCP scan types that you'll be using in Nmap. On the surface they seem to perform the same thing, however, they're very different. Before we break this down, let's illustrate TCP/IP's three-way-handshake again and recap the three stages of a "normal" three-way-handshake:

    SYN
    SYN/ACK
    ACK


(The Open University., N.D)

    Connect Scan - nmap -sT <ip>
    SYN Scan - nmap -sS <ip>

8.4.1.1 SYN Scan:

The most favourable type of scan, Nmap uses the TCP SYN scan (-sS) if the scan is run with both administrative privileges and a different type isn't provided. Unlike a connect scan, this scan type doesn't fulfil the "three-way-handshake" as what would normally take place. Instead, after the "SYN/ACK" is received from the remote host, a "RST" packet is sent by the host that we are scanning from (never completing the connection).

This scan type is the most favourable method as Nmap can use all the information gathered throughout the handshake to determine port status based on the response that is given by the IP address that is being scanned:

    SYN/ACK = open
    RST = Closed
    Multiple attempts = filtered

Not only this but also since fewer packets are sent across a network, there is less likelihood of being detected.

8.4.1.2. Connect Scan:

Unlike a SYN scan, administrative privileges aren't required for this scan to run. This is as a result of Nmap using the Berkeley Sockets API which has quickly formed to be the standard method of how services like web applications communicate with an operating system. As a result of more packets being sent by Nmap, this scan is easier to detect and takes a longer time to complete. Moreover, as the "three-way-handshake" completes as if it were a normal connection, it can be logged a lot more conveniently.

8.5. Nmap Timing Templates

Nmap allows the user to determine Nmap's performance. Measured in aggressiveness, a user can use one of six profiles [0 to 5] to change the rate at which Nmap scans at. With -T0 being the stealthiest, this profile scans one port every 5 minutes, whereas -T5 is considered both the most aggressive and potential to be inaccurate. This is because the -T5 waits a mere 0.3 seconds for the remote device to respond to a handshake. Factors such as those listed below determine how accurate these scans are:

    The resource usage a remote server is under. The higher usage, the slower it is to send a response to Nmap.
    The quality of the connection. If you have a slow or unstable connection, you are likely to miss responses if you are sending many packets at once.

Generally speaking, you will want to use low-aggressive profiles for real-world scenarios, however, in a lab environment where noise doesn't matter - high-aggressive profiles prove to be the quickest. For perspective, Nmap uses -T3 if no profile is provided. In a pentesting situation, you'd be inclined to use a lower value such as whereas in a lab environment, a higher value-T4 will suffice as stealth is not as critical.

8.6. An Introduction to Nmap's Scripting Engine

A recent addition to Nmap is the Nmap Scripting Engine or NSE for short. This feature introduces a "plug-in" nature to Nmap, where scripts can be used to automate various actions such as:

    Exploitation
    Fuzzing
    Bruteforcing

At the time of writing, the NSE comes with 603 scripts, which can be found here.

nsedoc
Nmaps NSE Documentation Page

Take for example the FTP ProFTPD Backdoor script. This script attempts to exploit an FTP service that is running ProFTPD version 1.3.3c, the version of which is fingerprinted by Nmap itself.

We can provide the script that we want to use by using the --script flag in Nmap like so:nmap --script ftp-proftpd-backdoor -p 21 <ip_address>

8.7. Additional Scan Types:

Not only can we use the Nmap's TCP Scan, but Nmap also boasts a combination of these types for various actions that are useful to us during the information gathering stage. I have assorted these into the table below, giving a brief explanation of their purpose.

(Where x.x.x.x == MACHINE_IP)
Flag 	Usage Example 	Description
-A 	Nmap -A x.x.x.x 	Scan the host to identify services running by matching against Nmap's database with OS detection
-O 	Nmap -O x.x.x.x 	Scan the host to retrieve and perform OS detection
-p 	nmap -p 22 x.x.x.x 	Scan a specific port number on the host
-p- 	nmap -p- 0-1000 x.x.x.x 	Provided a range of ports to scan.In our example, we scan 0-100, but just providing -p- will scan all ports (0-65535).
-sV 	nmap -sV x.x.x.x 	Scan the host using TCP and perform version fingerprinting
8.8. Defending against Nmap Scans

The practice of security through obscurity doesn't work here. Whilst it may seem logical to attempt to hide a service by changing its port number to something other than the standard (such as changing SSH from port 22 to 2222), the service will still be fingerprinted during an Nmap scan (albeit slightly later on). Unfortunately, you cannot get the best of both worlds in having a service available yet hidden.

Fortunately, open-source Intrusion Detection (IDS) & Prevention Systems (IPS) such as Snort and Suricata allows blue-teamers to protect their networks using network monitoring. For example, you would install these services on firewalls such as pfSense:

The dashboard of a pfSense Firewall.

Rulesets such as the emerging threats for Snort and Suricata are capable of detecting and blocking a wide variety of potentially malicious traffic - including:

    Malware traffic
    Reverse shells
    Metasploit payloads
    Nmap scans


A list of Snort rules installed on a pfSense firewall.

For example, detecting the Metasploit payload for CVE 2013-3205:

The emerging threat rule to detect the Metasploit payload for CVE-2013-3205.

If properly configured, a majority of Nmap scans can be detected. This is especially true when using an aggressive timing template such as -T4 or -T5. Let's take a look at the following Nmap scan being detected: nmap -A 192.168.171

Starting an Nmap scan to the pfSense firewall.

After returning to pfSense a few seconds later, we notice that alerts are being generated by Snort:

Viewing newly created alerts by Snort as a result of the Nmap scan.

Even with a timing template of-T3, Snort is capable of detecting the port scan, where after 6 alerts (in this case) the attacker is then blocked by the firewall.

After 6 alerts, Snort blocks the IP address running the Nmap scan from contacting the pfSense firewall.


Confirming that the IP address running the Nmap scan can no longer contact the pfSense firewall.

8.9. Challenge

Deploy and use Nmap to scan the instance attached to this task. Take a note of the IP address that you will need to scan: (MACHINE_IP) and enumerate it for Elf McEager!

Optional bonus: As a result of Elf McEager managing to recover christmas in "Day 8 - The Grinch Really Did Steal Christmas", TBFC's website has been restored for all the elves to visit. Can you find it? I hear it's quite the read... You must addMACHINE_IP tbfc.blog to your /etc/hosts file before the application will load like below:
hosts



-------------------------------------------------------------------------

When was Snort created?
'''
1998
'''

Using Nmap on MACHINE_IP, what are the port numbers of the three services running?  (Please provide your answer in ascending order/lowest -> highest, separated by a comma)
'''
80,2222,3389
'''


Run a scan and provide the -Pn flag to ignore ICMP being used to determine if the host is up
'''
no answer
'''


Experiment with different scan settings such as-A and -sV whilst comparing the outputs given.
'''
no answer
'''


Use Nmap to determine the name of the Linux distribution that is running, what is reported as the most likely distribution to be running?
'''
ubuntu
'''


Use Nmap's Network Scripting Engine (NSE) to retrieve the "HTTP-TITLE" of the webserver. Based on the value returned, what do we think this website might be used for?
'''
Blog
'''


Now use different scripts against the remaining services to discover any further information about them
'''
no answer
'''

