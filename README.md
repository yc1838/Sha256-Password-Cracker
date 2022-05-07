# sha256 password-cracker
 password cracker written in python

how to use pwcrack.py:
use python 3 to execute the pycrack.py file. The command line will ask for 3 things:
1. the hashed password you have, which only supports those that has been hashed in sha256 with the salt.
2. the salt for the password. If you have the hashed sha256 password, it is usually whatever is in front of the $
3. the txt format file with a list of potential passwords. We recommand you use the famous rockyou.txt file which can be found here: https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
Then the program will execute and will let you know if we have successfully found the original password through this list.

how to use pwcrack_online.py:
this only works with the gift card website project from https://github.com/moyix/appsec_hw2 
1. enter the username of the person which you are trying to crack their password.
2. enter the name of the file with the list of potential passwords. again rockyou.txt was used here.
Then the program will execute and will let you know if you have successfully found the original password through this list. Notice that since this password cracker program needs to talk with the website's api directly, the speed can be much slower than pwcrack.py.