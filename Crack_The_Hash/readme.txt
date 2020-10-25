					[Task 1] Level 1 

#1

Hash: 48bb6e862e54f2a795ffc4e541caed4d
'''
Answer: easy
'''

#2 	

Hash: CBFDAC6008F9CAB4083784CBD1874F76618D2A97 

Solution: Similar to Task 1-1, but the mode is (-m 100) for hashcat

Answer: password123

#3 	

Hash: 1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032

Solution: Similar to Task 1-1, but the mode is (-m 1400) for hashcat

Answer: letmein

#4 	

Hash: $2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom

Solution: This one is little bit tricky which is this hash cannot be cracked using online tool. That is why hashcat came in, set the mode to -m 3200

Answer: bleh

#5 	

Hash: 279412f945939ba78ce0758d3fd83daa

Solution: Similar to Task 1-1, but the mode is (-m 900) for hashcat

Answer: Eternity22 

					[Task 2] Level 2 

#1 	

HHash: F09EDCB1FCEFC6DFB23DC3505A882655FF77375ED8AA2D1C13F640FCCC2D0C85

Solution: Similar to Task 1-1, but the mode is (-m 1400) for hashcat

Answer: paule 

#2 	

Hash: 1DFECA0C002AE40B8619ECF94819CC1B

Solution: Similar to Task 1-1, but the mode is (-m 1000) for hashcat

Answer: n63umy8lkf4i 

#3 	

Hash: $6$aReallyHardSalt$6WKUTqzq.UQQmrm0p/T7MPpMbGNnzXPMAXi4bJMl9be.cfi3/qxIf.hsGpS41BqMhSrHVXgMpdjS6xeKZAs02.

Solution: This hash cannot be cracked using online tool but can be cracked using hashcat by setting the mode -m 1800. (It take some time).

Answer: waka99


#4 	

Hash: e5d8870e5bdd26602cab8dbe07a942c8669e56d6:tryhackme

Solution: This hash also cannot be cracked using online tool due to the present of salt ( tryhackme ). This only can be done by using hashcat with mode -m 110.

Answer: 481616481616