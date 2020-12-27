

One of the 'little helpers' logged into his workstation only to realize that the database connector file has been replaced, and he can't find the naughty list anymore. Furthermore, upon executing the database connector file, a taunting message was displayed, hinting that the file was moved to another location.

McEager has been notified, and he will put the pieces together to find the database connector file.

Watch DarkStar's Video On Solving The Task Here.

Task: Find where the database connector file is hidden using forensic-like investigative techniques.

You can use the AttackBox and Remmina to connect to the remote machine. Make sure the remote machine is deployed before proceeding.

Click on the plus icon as shown below.

For Server provide (MACHINE_IP) as the IP address provided to you for the remote machine. The credentials for the user account is:

    User name: littlehelper
    User password: iLove5now!

Accept the Certificate when prompted and you should be logged into the remote system now.

Note: The virtual machine may take up to 3 minutes to load.

We will continue our journey with Powershell. With Powershell, we can obtain file hashes of files on the endpoint.

A file hash, or simply a hash, is a mathematical algorithm that analyzes the data of the file and outputs a value, which is its hash.  File hashes let us know whether a file is legitimate or not based on its verified file hash. If the file has been replaced or altered, the file hash will be different. There are exceptions to this rule, but we will not dive into that. For now, it's safe to know that a file hash acts like a signature for a file.

With PowerShell, we can obtain the hash of a file by running the following command: Get-FileHash -Algorithm MD5 file.txt

By comparing the verified file hash to the above cmdlet's output, you will know whether the file is authentic.

At this point, you should be confident that the file sitting in the Documents folder is not legitimate. If you run the file, you can see that not much information is given, only the hint that the original file was moved to another location within the endpoint.

Another tool you can use to inspect within a binary file (.exe) is Strings.exe. Strings scans the file you pass it for strings of a default length of 3 or more characters. You can use the Strings tool to peek inside this mysterious executable file. The tool is located within C:\Tools.

The command to run for the Strings tool to scan the mysterious executable: c:\Tools\strings64.exe -accepteula file.exe

In the output, you should notice a command related to ADS. You know this by the end of the Powershell command -Stream.

Alternate Data Streams (ADS) is a file attribute specific to Windows NTFS (New Technology File System). Every file has at least one data stream ($DATA) and ADS allows files to contain more than one stream of data. Natively Window Explorer doesn't display ADS to the user. There are 3rd party executables that can be used to view this data, but Powershell gives you the ability to view ADS for files.

Malware writers have used ADS to hide data in an endpoint, but not all its uses are malicious. When you download a file from the Internet unto an endpoint there are identifiers written to ADS to identify that it was downloaded from the Internet.

The command to view ADS using Powershell: Get-Item -Path file.exe -Stream *

There are a few lines of output when you run this command. Pay particularly close attention to Stream and Length.

Recall that the database connector file is an executable file, and it's hidden within an alternate data stream for another file. We can use a built-in Windows tool, Windows Management Instrumentation, to launch the hidden file.

The command to run to launch the hidden executable hiding within ADS: wmic process call create $(Resolve-Path file.exe:streamname)

Note: You must replace file.exe with the actual name of the file which contains the ADS, and streamname is the actual name of the stream displayed in the output.

------------------------------------------------------------------------

Read the contents of the text file within the Documents folder. What is the file hash for db.exe?
'''
'''


What is the file hash of the mysterious executable within the Documents folder?
'''
'''


Using Strings find the hidden flag within the executable?
'''
'''


What is the flag that is displayed when you run the database connector file?
'''
'''

