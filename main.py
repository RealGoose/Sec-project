import os
import time

def start():
    print("Welcome!\n")

    print("Choices: \n-h   Help Menu\n-l   Show change logs\n-sp  Scan the host for open ports\n-sv  Scan the host for vulnerabilities\n-bp  Scan the host for Best Practices violations\n-un  Uninstall used packages and modules")
    choice = input("")
    
    if (choice == "-h"):
        help()

    elif (choice == "-l"):
        logs()

    elif (choice == "-sp"):
        ports()

    elif (choice == "-sv"):
        vulns()

    elif (choice == "-bp"):
        BestPractices()

    elif (choice == "-un"):
        uninstallPackages()

    else:
        print("Invalid Input\nExiting...")
    


def help():
    print("You chose the help menu")

def logs():
    print("You chose #2")

def ports():
    print("You chose #3")

def vulns():
    print("You chose #4")

def BestPractices():
    print("You chose #4")


def installpackages():
    '''Install the needed packages using pip, will install pip, nmap, and others needed. Must be run before the choices. Will run automatically.'''
    #os.system("echo Hello from the other side!")
    
    pip_install = os.system("pip install pip")
    print("`pip install pip` ran with exit code %d" % pip_install)

    nmap_install = os.system("pip install python-nmap")
    print("`pip install python-nmap` ran with exit code %d" % nmap_install)


def uninstallPackages():
    '''Uninstall the packages using pip. Won't be run unless called by user. Will only uninstall packages installed in the installpackages().'''
    #os.system("echo Hello from the other side!")
    
    pip_uninstall = os.system("pip uninstall pip")
    print("`pip uninstall pip` ran with exit code %d" % pip_uninstall)

    nmap_uninstall = os.system("pip uninstall python-nmap")
    print("`pip uninstall python-nmap` ran with exit code %d" % nmap_uninstall)    











start()  
