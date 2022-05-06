# sha256 password-cracker
 password cracker written in python

how to use:
use python 3 to execute the pycrack.py file. The command line will ask for 3 things:
1. the hashed password you have, which only supports those that has been hashed in sha256 with the salt.
2. the salt for the password. If you have the hashed sha256 password, it is usually whatever is in front of the $
3. the txt format file with a list of potential passwords. We recommand you use the famous rockyou.txt file which can be found here: https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
Then the program will execute and will let you know if we have successfully found the original password through this list.