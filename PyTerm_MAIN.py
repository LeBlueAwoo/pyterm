#Import modules
import time, os, datetime, getpass, socket

#Clear the screen and show intro
os.system("clear")
print("Welcome to PyTerm 2.0! See CHANGELOG.txt for details.", end="")

while True:
    #Set variables
    cwd=os.path.dirname(os.path.realpath(__file__))
    time=datetime.datetime.now()
    user=getpass.getuser()
    host=socket.gethostname()

    #Show command prompt
    print("\n[" + user + "@" + host + ":~" + cwd + "]-[", end="")
    print(time.strftime("%H:%M:%S") + "]")
    cmd=input(">$ ")

    #Change directory if necessary, otherwise execute the contents of 'cmd'
    if cmd==("cd"):
        cd=input("Go to: ")
        os.chdir(cd)
    else:
        os.system(cmd)
