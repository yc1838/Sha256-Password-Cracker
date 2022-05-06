from binascii import hexlify
from hashlib import sha256
from os import urandom, system
import sys, os
import random
import time


# TARGET = "000000000000000000000000000078d2$18821d89de11ab18488fdc0a01f1ddf4d290e198b0f80cd4974fc031dc2615a3"
# PRE_DEFINIED_SALT = "000000000000000000000000000078d2"
# file_name = "rockyou.txt"

def split_salt_and_hashed_password(combined):
    splited_1, splited_2 = combined.split("$")
    return splited_2


def try_passwords(pword, target, salt):
    #this salt is in bytes.
    hasher = sha256()
    hasher.update(salt)
    hasher.update(pword.encode('utf-8'))
    final_password = hasher.hexdigest()
    if final_password == target:
        return True
    else:
        return False


def read_file(file_name, target, salt):
    with open(file_name, encoding = 'koi8_u') as f:
        all_lines = f.readlines()
    count = 0
    for line in all_lines:
        pword = line.strip()
        count += 1
        if (try_passwords(pword, target, salt) == True):
            return line, count
    return None

#ask for file name
#ask for salt and hashed password, update these as constant.
target_input = input("Please put in the target hashed password first: \n")
target_input = target_input.strip()
salt_input = input("Please enter the salt: \n")
salt_input = salt_input.strip()
file_name = input("Please enter the file name and it has to be in the same directory: \n")
file_name = file_name.strip()

target = split_salt_and_hashed_password(target_input)
salt = bytes(salt_input, encoding='utf-8')
start = time.time()
result, count = read_file(file_name, target, salt)
end = time.time()
time_lapsed = end - start
time_lapsed = round(time_lapsed, 2)
guess_per_second = round(count/time_lapsed, 2)
print("time lapsed is " + str(time_lapsed) + " seconds.")
print("average guess per second is " + str(guess_per_second))
if result != None:
    print("We found the password which is " + result.strip())
else:
    print("we did not find anything.")

