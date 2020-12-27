

Someone is mischievous at The Best Festival Company. The contents within the stockings have been removed. A clue was left in one of the stockings that hints that the contents have been hidden within Elfstation1. McEager moves quickly and attempts to RDP into the machine. Yikes! He is unable to log in.

Luckily, he has been learning PowerShell, and he can remote into the workstation using PowerShell over SSH.

Task: Use the PowerShell console to navigate throughout the endpoint to find the hidden contents to reveal what was hidden in the stockings.

Watch JohnHammond's video on solving this task!

You will use SSH to connect to the remote machine.

The command to run to connect to the remote machine: ssh -l mceager MACHINE_IP

Note that your IP address will be different. When prompted, enter the password: r0ckStar!

If you logged in successfully, you will see the following prompt.

Before we begin, launch PowerShell and navigate to the Documents folder.



Note: The virtual machine may take up to 3 minutes to load.

The official explanation of PowerShell is: "PowerShell is a cross-platform task automation and configuration management framework, consisting of a command-line shell and scripting language. Unlike most shells, which accept and return text, PowerShell is built on top of the .NET Common Language Runtime (CLR), and accepts and returns .NET objects. This fundamental change brings entirely new tools and methods for automation."

PowerShell has grown in popularity in the last few years among defenders and especially attackers. Knowing PowerShell is a necessary skill. If you have only heard of PowerShell but never dabbled with it, fret not, today you will.

Recall from the definition above that PowerShell is a command-line shell. We must enter commands into the command prompt to instruct PowerShell on what we want it to do for us. PowerShell commands are known as cmdlets.

To list the contents of the current directory we are in, we can use the Get-ChildItem cmdlet.  There are various other options we can use with this cmdlet to enhance its capabilities further.

    -Path Specifies a path to one or more locations. Wildcards are accepted.
    -File / -Directory To get a list of files, use the File parameter. To get a list of directories, use the Directory parameter. You can use the Recurse parameter with File and/or Directory parameters.
    -Filter Specifies a filter to qualify the Path parameter.
    -Recurse Gets the items in the specified locations and in all child items of the locations.
    -Hidden To get only hidden items, use the Hidden parameter.
    -ErrorAction SilentlyContinue Specifies what action to take if the command encounters an error.

For example, if you want to view all of the hidden files in the current directory you are in, you can issue the following command: Get-ChildItem -File -Hidden -ErrorAction SilentlyContinue

Another useful cmdlet is Get-Content. This will allow you to read the contents of a file.

You can run this command as follows: Get-Content -Path file.txt

You can run numerous operations with the Get-Content cmdlet to give you more information about the particular file you are inspecting. Such as how many words are in the file and the exact positions for a particular string within a file.

To get the number of words contained within a file, you can use the Get-Content cmdlet and pipe the results to the Measure-Object cmdlet.

You run this command as follows: Get-Content -Path file.txt | Measure-Object -Word

To get the exact position of a string within the file, you can use the following command:  (Get-Content -Path file.txt)[index]

The index is the numerical value that is the location of the string within the file. Since indexes start at zero, you typically need to subtract one from the original value to extract the string at the correct position. This is not necessary for this exercise.

To change directories, you can use the Set-Location cmdlet.

For example, Set-Location -Path c:\users\administrator\desktop  will change your location to the Administrator's desktop.

The last cmdlet that is needed to solve this room is Select-String. This cmdlet will search a particular file for a pattern you define within the command to run.

An example execution of this command is: Select-String -Path 'c:\users\administrator\desktop' -Pattern '*.pdf'

Note: You can always use the Get-Help cmdlet to obtain more information about a specific cmdlet. For example, Get-Help Select-String


---------------------------------------------------------------------------


Search for the first hidden elf file within the Documents folder. Read the contents of this file. What does Elf 1 want?
'''
2 front teeth
'''


Search on the desktop for a hidden folder that contains the file for Elf 2. Read the contents of this file. What is the name of that movie that Elf 2 wants?
'''
Scrooged
'''


Search the Windows directory for a hidden folder that contains files for Elf 3. What is the name of the hidden folder? (This command will take a while)
'''
3lfthr3e
'''


How many words does the first file contain?
'''
9999
'''


What 2 words are at index 551 and 6991 in the first file?
'''
Red Ryder
'''


This is only half the answer. Search in the 2nd file for the phrase from the previous question to get the full answer. What does Elf 3 want? (use spaces when submitting the answer)
'''
red ryder bb gun
'''