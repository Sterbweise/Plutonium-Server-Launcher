#!/usr/bin/python

import os
import sys
import traceback

Server = [["name","key","port","cfg","path"]]
cmd = [""]*99
bindir = [""]
    

if os.getuid() != 0:
    print("Sorry. This script requires sudo privledges")
    sys.exit()


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
 \033[1;32m[ Black Ops 2 Servers Launcher ] \033[1;m
		''')
    if (bindir is not None):
        def menu():
            while True:
                print('''
1) Launch Server
2) Add New Server
3) More Tools
4) Help
			''')

                Option = input("\033[1;36m > \033[1;m")

                while Option == "1":
                    for i in range (0,len(servmulti),1):
                        tri = str(i)
                        tri1 = str(i + 1)
                        print(tri + ") " + servmulti[i] )
                    print(tri1 + ") All")

                    repo = input("\033[1;32m Server Number > \033[1;m")
                    
                    for j in range(0,99,1):
                        if repo == str(j):
                            cmd[j] = os.system("cd " + bindirectory[j] + " && wine .\\bin\\plutonium-bootstrapper-win32.exe t6zm " + serverdirectory[j] + " -dedicated +start_map_rotate +set key " + key[j] + " +set net_port " + port[j] + " +set sv_config " + cfg[j] )
                        
                        elif repo == "back":
                            menu()
                        elif repo == "gohome":
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
                    for i in range (0,len(servmulti),1):
                        tri = str(i)
                        tri1 = str(i + 1)
                        print(tri + ") " + servmulti[i] )
                    print(tri1 + ") All")

                    repo = input("\033[1;32m Server Number > \033[1;m")
                    
                    for j in range(0,99,1):
                        if repo == str(j):
                            cmd[j] = os.system("cd " + bindirectory[j] + " && wine .\\bin\\plutonium-bootstrapper-win32.exe t6zm " + serverdirectory[j] + " -dedicated +start_map_rotate +set key " + key[j] + " +set net_port " + port[j] + " +set sv_config " + cfg[j] )
                        
                        elif repo == "back":
                            install()
                        elif repo == "gohome":
                            install()

                            print (file.read())
                        else:
                            print ("\033[1;31mSorry, that was an invalid command!\033[1;m") 					


        install()
    except KeyboardInterrupt:
        print ("Shutdown requested...Goodbye...")
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)

if __name__ == "__main__":
    main()
