					




					Task 1 Preparation





					

Installing the Required Software

Each year millions of home routers are sold to consumers, a large majority of them don't even know whats running on them. Today we're going to take a look. Before proceeding we will need a few tools:

    Access to a Linux distribution (Or WSL) with strings and binwalk on it.
    Linksys WRT1900ACS v2 Firmware found here: https://github.com/Sq00ky/Dumping-Router-Firmware-Image/
    Lastly, ensure binwalk has JFFS2 support with the following command:

sudo pip install cstruct 

git clone https://github.com/sviehb/jefferson

cd jefferson && sudo python setup.py install

After you've got the tools, you're ready to setup your work space!

Rebuilding the Firmware

First, we're going to clone the repository that holds the firmware:

git clone https://github.com/Sq00ky/Dumping-Router-Firmware-Image/ /opt/Dumping-Router-Firmware && cd /opt/Dumping-Router-Firmware/

Next, we're going to unzip the multipart zip file:

7z x ./FW_WRT1900ACSV2_2.0.3.201002_prod.zip

running an ls you should see the firmware image:

FW_WRT1900ACSV2_2.0.3.201002_prod.img

 Lastly, running a sha256sum  on the firmware image you should be left with the value dbbc9e8673149e79b7fd39482ea95db78bdb585c3fa3613e4f84ca0abcea68a4


Answer the questions below

Download the firmware and get your work space setup!
'''
no answer
'''






					Task 2 Investigating Firmware









One Inch Deep Analysis

In this section we will be taking a look at the firmware, checking for strings and, dump the file system from the image. The next section will cover mounting and exploring the file system.
Answer the questions below

While running a strings on the file, there is a lot of notable clear text. This is due to certain aspects of the firmware image not being encrypted. This likely means that with Binwalk, we will be able to dump the firmware from the image.


Running strings on the file, what does the first clear text line say?
'''
Linksys WRT1900ACS Router
'''


Also using strings, what operating system is the device running?
'''
linux
'''


Scrolling through with strings, you may notice some other interesting lines like 

/bin/busybox

and various other lua files. It really makes you wonder whats going on inside there...
'''
no answer
'''


Next we will be dumping the filesystem from the image file. To do so, we will be using a tool called binwalk.

Binwalk is a tool that checks for well known file signatures within a given file. This can be useful for many things, it even has its uses in Steganography. A file could be hidden within the photo and Binwalk would reveal that, and help us extract it. We will be using it to extract the filesystem of the router in this instance.
'''
no answer
'''


What option within Binwalk will allow us to extract files from the firmware image?
'''
-e
'''


Now that we know how to extract the contents of the firmware image, what was the first item extracted?
'''
uImage header
'''


What was the creation date?
'''
2020-04-22 11:07:26
'''


The Cyclical Redundancy Check is used in a similar way that file hashing is, to ensure that the file contents were not corrupted and or modified in transit.


What is the CRC of the image?
'''
0xABEBC439
'''


What is the image size?
'''
4229755 bytes
'''


What architecture does the device run?
'''
arm
'''


Researching the results to question 10, is that true?
'''
yes
'''

You will notice two files got extracted; one being the jffs2 file system and another that Binwalk believes it to be gzip compressed data.


You can attempt to extract the data, however, you won't get anywhere. Binwalk misinterpreted the data, however, we can still do some analysis of it.


Running strings on 6870, we notice a large chunk of clear text. We can actually run binwalk again on this file to receive even more files to investigate. Interestingly enough, a copy of the Linux kernel is included. What version is it for?
'''
3.10.39
'''


If you run extract the contents of 6870 with Binwalk and run strings on 799E38.cpio, you may see a lot of hex towards the bottom of the file. Some of it can be translated into human readable text. Some of it is interesting to see and really makes you wonder what its purpose was for. Maybe some additional investigation will reveal its purpose. I will leave you to explore that on your own though :)
'''
no answer
'''


Continuing on with the analysis, we have a jffs2 file system that we can examine the contents of. First, we need to mount it though, which brings us into the next section
'''
no answer
'''
		




					Task 3 Mounting and Analysis of the Router's Filesystem 






Mounting the Filesystem

In this section, we will begin to go over how to mount the file system. Note, if you are doing this with any other file system and it is not in the Little Endian format, you will need to convert it from Big Endian to little Endian using a tool called jffs2dump. But here is my fairly concise guide to mounting the filesystem:

Step 1. If /dev/mtdblock0 exists, remove file/directory and re-create the block device

rm -rf /dev/mtdblock0
mknod /dev/mtdblock0 b 31 0
Step 2. Create a location for the jffs2 filesysystem to live
mkdir /mnt/jffs2_file/
Step 3. Load required kernel modules
modprobe jffs2
modprobe mtdram
modprobe mtdblock
Step 4. Write image to /dev/mtdblock0
dd if=/opt/Dumping-Router-Firmware-Image/_FW_WRT1900ACSV2_2.0.3.201002_prod.img.extracted/600000.jffs2 of=/dev/mtdblock0
Step 5. Mount file system to folder location
mount -t jffs2 /dev/mtdblock0 /mnt/jffs2_file/
Step 6. Lastly, move into the mounted filesystem.
cd /mnt/jffs2_file/

To explain a little bit of what the command does, we're creating a block device (mtdblock (Memory Technology Device)) that will allow us to dump the flash memory. We're first removing it if it exists, and then re-creating it.

Next, we're creating a location for our jffs2 file to be mounted to.

After that we're loading some kernel modules that will allow us to interact with the jffs2 file system and dump the flash memory.

Next, we are writing the file system to the block device, and after that we are mounting the mtdblock device
which now contains the flash memory of the file system . 

Lastly, executing  cd /mnt/jffs2_file/ we are now sitting inside the routers dumped firmware and can begin investigation.
Answer the questions below

Running an ls -la reveals a lot of interesting information. First we notice that a lot of files are symbolically linked (which is similar to a shortcut). 

Where does linuxrc link to?

What parent folder does mnt, opt, and var link to?

What folder would store the routers HTTP server?

Scanning through a lot of these folders, you may begin to notice that they are empty. This is extremely strange, but that is because the router is not up and running. Remember, we are mearly looking at a template of the filesystem that is going to be flashed onto the router, not the firmware from a router that has been dumped. Other information about the router may be contained in the previous section within the 6870 block.


The first of the folders that isn't empty is /bin/, where do a majority of the files link to?

Why is that? Well, busybox is more or less a tool suite of common executable commands within the Unix environment.

Within the bin folder, interestingly enough, what database would be running if the router was online?

The next notable folder of interest is /etc/. This folder contains a lot of configuration files for the router, such as Access Point power levels regulated by certain countries. One you might recognize is the FCC (Federal Communications Commission).

We can even see the build date of the device. What is the build date? 

There are even files related to the SSH server on the device. What SSH server does the device run?

We can even see the file for the media server, which company developed it?

This company use to own Linksys at one point in time, which is likely why it is still being used.

Which file within /etc/ contains a list of common Network services and their associated port numbers?

Which file contains the default system settings?

Within the /etc/ folder, what is the version specific firmware version?

Backing out into the JNAP folder, the JNAP API (formerly known as HNAP, the Home Network Administration Protocol) has been a potential attack vector and vulnerability in the past, which this article highlights here. Interestingly enough, reminense of it is still here today on Linksys devices. Going to  http://<Default_Gateway>/JNAP/ on a Linksys router reveals an interesting 404. Much different than the standard 404.

Accessing /JNAP/

Accessing any other invalid URI

which makes you wonder if something is still really there. If you investigate within /JNAP/modules folder back on the dumped filesystem, you will see some contents related to the device and what services it offers, some of them are firewalls, http proxies, QoS, VPN servers, uPnP, SMB, MAC filtering, FTP, etc.


Side note: If you have a Linksys router and are interested in playing around further, I found this Github Repository for tools to interact with JNAP, I chose not to include this within the room since not everyone has access to a Linksys router. I won't go much further than exploring the File System. 


What 3 networks have a folder within /JNAP/modules?

After then JNAP folder, lib is the only other folder that really has any contents whatsoever and whats in there is pretty standard in terms of libraries. The rest of the file system is relatively bare which leads us to the end of this room.

I hope I made you all a little bit more curious about whats going on in your device, most importantly I hope you enjoyed. I encourage all of you to go out on your own and get your own router's Firmware and do some firmware dumping and take a look at whats going on inside your device.

A room about Cable Modems may come in the future, however, Cable Modems firmware images are relatively difficult to get your hands on since they are only distributed to CMOs (Cable Modem Operators, like Charter, XFinity, Cox, etc.)
