#!/usr/bin/python

import os
import sys
import traceback


Server = [["name","key","port","cfg","gamemode","path"]]*99
cmd = [""]*99
Bindir = "" 

if os.getuid() != 0 :
    print("Sorry. This script requires sudo privledges")
    sys.exit()

def ReadBin():
    with open ("Bin.txt", "r+") as Bin:
        Bindir = Bin.readlines()
        Bin.close()
    
def ReadServer():
    with open ("ServerConfig.txt", "r+") as ServerConfig:
        for i in (0, len(ServerConfig),1):
            Server[i] = ServerConfig.readline(i)
            ServerConfig.close()

def Binmodif():
    Binset = input("\033[1;36m Enter your Plutonium Binary Path > \033[1;m")
    with open ("Bin.txt", "w+") as Bin:
        Bin.write(Binset)
        Bin.close

def SetServer():
    with open ("ServerConfig.txt", "w+") as SetServer:
        for i in range (0,len(Server),1):
            SetServer.write(Server[i] + "\n")
        SetServer.close
 
def main():
    try:
        print(''' \033[1;31m
 _____       ___   _____   _____   _   _____  __    __
/  ___|     /   | /  ___/ /  ___/ | | |  _  \ \ \  / /
| |        / /| | | |___  | |___  | | | | | |  \ \/ /
| |       / / | | \___  \ \___  \ | | | | | |   \  /
| |___   / /  | |  ___| |  ___| | | | | |_| |   / /
\_____| /_/   |_| /_____/ /_____/ |_| |_____/  /_/

 \033[1;32m[ Author: Minami.Xan | Github: https://github.com/Minami-xan] \033[1;m
 \033[1;32m[ T6 Servers Launcher ] \033[1;m
		''')
        if (os.path.exists("ServerConfig.txt") and os.path.exists("Bin.txt")):
            def menu():
                ReadBin()
                ReadServer()
                while True:
                    print('''
1) Launch Server
2) Add New Server
3) More Tools
4) Help
			''')

                    Option = input("\033[1;36m > \033[1;m")

                    while Option == "1":
                        for i in range (0,len(Server),1):
                            print(str(i) + ") " + Server[i][0] )
                        print(str(i + 1) + ") All")

                        repo = input("\033[1;32m Server Number > \033[1;m")
                        
                        for j in range(0,99,1):
                            if repo == str(j):
                                cmd[j] = os.system("cd " + Bindir + " && wine .\\bin\\plutonium-bootstrapper-win32.exe " + Server[j][4] + Server[j][5] + " -dedicated +start_map_rotate +set key " + Server[j][1] + " +set net_port " + Server[j][2] + " +set sv_config " + Server[j][3])
                            elif repo == "back":
                                menu()
                            elif repo == "home":
                                menu()
                                print (file.read())
                            else:
                                print ("\033[1;31mSorry, that was an invalid command!\033[1;m") 	

                    while Option == "2":
                        name = input("\033[1;32m Enter the of your Server > \033[1;m")
                        
                        for j in range(0,99,1):
                            if repo == str(j):
                                cmd[j] = os.system("cd " + Bindir + " && wine .\\bin\\plutonium-bootstrapper-win32.exe " + Server[j][4] + Server[j][5] + " -dedicated +start_map_rotate +set key " + Server[j][1] + " +set net_port " + Server[j][2] + " +set sv_config " + Server[j][3])
                            elif repo == "back":
                                menu()
                            elif repo == "home":
                                menu()
                                print (file.read())
                            else:
                                print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

            menu()
        else:

            def install():
                while True:
                    print('''
    1) Set Plutonium binary path
    2) Add New Server
    3) More Tools
    4) Help
                ''')
                    Option = input("\033[1;36m > \033[1;m")

                    while Option == "1":
                        Binmodif()
                        print('Your Plutonium Binary Path is Updated')
                        main()				
            install()

    except KeyboardInterrupt:
        print ("Shutdown requested...Goodbye...")
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)

if __name__ == "__main__":
    main()
