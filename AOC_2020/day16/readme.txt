Created by Bee.

Oh no! Santa 🎅 has taken off, leaving you -- the faithful elves behind! Can you help find Santa's location?

Luckily, the elves are OSINT masters and remember a thing or two. Specifically, they remember:

    Santa has a webpage at 10.10.90.199/static/index.html to help lost elves find their way home. Santa never told the elves what port number the webserver is on. Can you find out?!
    This webpage has a link somewhere on it, hidden away so anyone that isn't an elf can't find it.
    Santa's Sled has an API we can talk too. The key for the API is between 0 and 100, and it's an odd number. But be careful! After an unknown number of attempts, Santa's Sled will ban your IP address. 

Deploy the machine that is running Santa's Sled and allow a couple of minutes for the target (10.10.90.199) to start up. Using your Python skills from Day 15 to find the correct key for the API.

Watch John Hammonds video on solving this task!


---------------------------------------------------------------------

What is the port number for the web server?
'''
8000
'''


What is the directory for the API, without the API key?
'''
/api/
'''


Where is Santa right now?
'''
Winter Wonderland, Hyde Park, London
'''



Find out the correct API key. Remember, this is an odd number between 0-100. After too many attempts, Santa's Sled will block you. 

To unblock yourself, simply terminate and re-deploy the target instance (10.10.90.199)
'''
57
'''

