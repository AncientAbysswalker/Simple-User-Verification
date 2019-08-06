# Simple User Verification

## Problem Statement
This project arose from my thoughts on user verification for a given software. Let's say that we have a software wants to verify that a person has the right (license) to use a software package. This has been done for a while in various different ways by different software packages.

I began thinking about this problem and how one might go about implementing this verification. 

NOTE: This project is not really for implementation but more of a fun thought experiment for me to play with some of these concepts on a more base level, while alternate methodologies such as SSH are likely better implementations. Protecting software in this manner isn't always the best way to protect your code, which is why many companies are moving more towards SaaS. Python in particular is fairly easy to decompile, and as such these methods will not protect an application very well.
## Solution
I considered a few different methods of verification and settled on trying using a username and password pair with sockets. A username and password pair (theoretically) allows control over who uses the software, and having an external server verify the login helps to prevent license cracking.

My solution sends the username and password to the server, along with a random set of 64 bytes. The server recieves this login pair and checks that the username and SHA256 hash of the password are in the database (hashed password for security; I could use a salt if I wanted more security). If they are in the database, we will hash the random number and some other information and return this information through the socket to the client (to make it more difficult to bypass verification by network traffic manipulation). The client then verifies that this returned data matches what it expects to see.  