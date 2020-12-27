

The past few days there have been strange things happening at Best Festival Company. McEager hasn't had the time to fully investigate the compromised endpoints with everything that is going on nor does he have the time to reimage the workstations. McEager decides to log into a different workstation, one of his backup systems.

McEager logs in and to his dismay he can't log into his password manager. It's not accepting his master key! He notices that the folder name has been renamed to something strange.

Task: You must gain access to the password manager and decode the values within the password manager using CyberChef.

Watch John Hammond solve this task!

You can use the AttackBox and Remmina to connect to the remote machine. Make sure the remote machine is deployed before proceeding.

Click on the plus icon as shown below.

For Server provide (MACHINE_IP) as the IP address provided to you for the remote machine. The credentials for the user account is:

    User name: Administrator
    User password: sn0wF!akes!!!

Accept the Certificate when prompted and you should be logged into the remote system now.

Note: The virtual machine may take up to 3 minutes to load.

Password managers are the norm these days. There are many cloud-based password managers but there also are password managers you run locally on your endpoint, such as KeePass. KeePass is an executable that allows you to store all types of data, including passwords, in a password-protected database. The official definition of KeePass from its website:

"Today, you have to remember many passwords. You need a password for a lot of websites, your e-mail account, your webserver, network logins, etc. The list is endless. Also, you should use a different password for each account, because if you would use only one password everywhere and someone gets this password, you would have a problem: the thief would have access to all of your accounts. KeePass is a free open source password manager, which helps you to manage your passwords in a secure way. You can store all your passwords in one database, which is locked with a master key. So you only have to remember one single master key to unlock the whole database."

Now with that out of the way, open the strange-looking folder name on the desktop and run KeePass. You will be prompted to enter the master password. If you enter the phrase mceagerrockstar you will see a message stating that the key is invalid.

Looking back at the folder name it looks cryptic, like some sort of encoding. Encryption and encoding are familiar techniques used in IT, especially within Computer Security. Malware writers use some of these encoding techniques to hide their malicious code. Some encodings are quickly identifiable and some are not.

You can use CyberChef to decrypt/decode the encrypted/encoded values that you will encounter within this endpoint. CyberChef is the self-purported 'Cyber Swiss-Army Knife' created by GCHQ. It's a fantastic tool for data transformation, extraction & manipulation in your web-browser. CyberChef uses recipes to perform this magic.

Speaking of 'magic', you can use the Magic recipe to decode the folder name. There is a local copy of CyberChef (C:\Tools) on the endpoint.

To use a recipe simply drag and drop it into the Recipe window. Auto Bake should be checked of which will automatically run the recipe against the encoded value. If it is not checked, simply press BAKE!

Now that you have unlocked KeePass, you should see that there are more encodings within the KeePass database file. Take a close look at the Notes for each entry. They will provide clues on how to decode them. Some of the popular encodings are listed under Favourites. (HINT)

Note: To view the Password entries, click on the ellipsis [...].

Malware writers perform various iterations of encoding to frustrate the reverse engineering process. With that being said, one of the encoded values will require you to run the duplicate recipe 2x to get the fully decoded value. (HINT)


What is the password to the KeePass database?
'''
thegrinchwashere
'''


What is the encoding method listed as the 'Matching ops'?
'''
Base64
'''


What is the decoded password value of the Elf Server?
'''
sn0wM4n!
'''


What is the decoded password value for ElfMail?
'''
ic3Skating!
'''


Decode the last encoded value. What is the flag?
'''
THM{657012dcf3d1318dca0ed864f0e70535}
'''

