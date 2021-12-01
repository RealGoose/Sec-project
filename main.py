import os
import time

def start():
    print("Welcome!\n")

    print("Choices: \n-h   Help Menu\n-l   Show change logs\n-sp  Scan the host for open ports\n-sv  Scan the host for vulnerabilities\n-bp  Scan the host for Best Practices violations\n-un  Uninstall used packages and modules")
    print("\nYour Choice: ")
    
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
    print("\n\nYou chose the help menu, let me explain what this program is about and how it works :)\n")
    print("-h   Will call this menu which will explain what each of the options do and how to access the results.")
    print("-l   Will show logs from the run commands and how to access them")
    print("-sp  Will scan the host for open ports using nmap and will display them on your screen. See what open ports mean here: https://en.wikipedia.org/wiki/Open_port")
    print("-sv  Will scan the host using the nmap vuln scanner. This scan shows basic vulnerabilities and the results will be outputted to a separate file.")
    print("-bp  Will scan for Best Practices on your computer. These include default and unsecure passwords, disabled firewall, outdated software, etc.")
    print("-un  Will uninstall the modules which were installed to conduct scans on the machine. Includes nmap, pip, etc.")
    print("\nHope this cleared everything up!")


def logs():
    print("You chose #2")

def ports():
    print("----------------------------------------------------------------------")
    print("PORT SCANNING OPTION SELECTED:")

    os.system("nmap 192.168.136.134")



def vulns():
    print("INSTALLING PACKAGES AND RUNNING VULNERABILITY SCAN")

    installpackages()

     

    os.system("nmap -sV --script=vulscan/vulscan.nse 192.168.136.134")

    os.system("nmap --script nmap-vulners/ -sV 192.168.136.134")



def BestPractices():
    print("You chose #4")


def installpackages():
    '''Install the needed packages using pip, will install pip, nmap, and others needed. Must be run before the choices. Will run automatically.'''
    #os.system("echo Hello from the other side!")
    
    print("\nINSTALLING PIP:\n")
    pip_install = os.system("pip install pip")
    print("`pip install pip` ran with exit code %d" % pip_install)

    print("\nINSTALLING NMAP:\n")
    nmap_install = os.system("pip install python-nmap")
    print("`pip install python-nmap` ran with exit code %d" % nmap_install)

    print("\nINSTALLING VULSCAN:\n")

    os.system("cd /usr/share/nmap/scripts/")
    vulscan_install = os.system("git clone https://github.com/scipag/vulscan scipag_vulscan")
    os.system("sudo ln -s `pwd`/scipag_vulscan /usr/share/nmap/scripts/vulscan")

    print("\nINSTALLING VULNERS:\n")

    os.system("cd /usr/share/nmap/scripts/")
    vulners_install = os.system("git clone https://github.com/vulnersCom/nmap-vulners.git")






def uninstallPackages():
    '''Uninstall the packages using pip. Won't be run unless called by user. Will only uninstall packages installed in the installpackages().'''
    #os.system("echo Hello from the other side!")
    
    pip_uninstall = os.system("pip uninstall pip")
    print("`pip uninstall pip` ran with exit code %d" % pip_uninstall)

    nmap_uninstall = os.system("pip uninstall python-nmap")
    print("`pip uninstall python-nmap` ran with exit code %d" % nmap_uninstall)    











start()  
