#!/usr/bin/env python3
from os import system as sh

d = print('\n----------------------\n> O.B.C. Terminal\n----------------------\n> OPTIONS:\n> 1: Fingerprint\n> 2: PortScan\n> 3: Vulncannon\n> 4: Exit\n')

while True:
    ui = input("")
    if ui == "EXIT" or ui == "exit" or ui=="4" or ui==4:
        print('\n----------------------\n> Engagement Completed\n')
        break
    elif ui == "1" or ui == 1:
        a = print('\n----------------------\n> Orbital Beam Online & Ready\n-----------------------')
        b = sh('echo "> Target Range?\n " && read ip && echo "> Target Name?\n" && read target && sudo nmap -A -O -n -p- -oN "~/.obc/recon/$target.txt" $ip > /dev/null 2>&1')
        c = print('\n----------------------\n> Target Recon Completed.\n')
        d = print('\n----------------------\n> O.B.C. Terminal\n----------------------\n> OPTIONS:\n> 1: Fingerprint\n> 2: PortScan\n> 3: Vulncannon\n> 4: Exit\n')
    elif ui == "2" or ui == 2:
        a = print('\n----------------------\n> Orbital Beam Online & Ready\n-----------------------')
        b = sh('echo "> Target Range?\n " && read ip && echo "> Target Name?\n" && read target && sudo nmap -p0-65535 -oN "~/.obc/recon/$target.txt" $ip > /dev/null 2>&1')
        c = print('\n----------------------\n> Target(s) Identified Completed.\n')
        d = print('\n----------------------\n> O.B.C. Terminal\n----------------------\n> OPTIONS:\n> 1: Fingerprint\n> 2: PortScan\n> 3: Vulncannon\n> 4: Exit\n')
    elif ui == "3" or ui == 3:
        a = print('\n----------------------\n> Orbital Beam Online & Ready\n-----------------------')
        b = sh('echo "> Target?\n " && read ip && echo "> Target Name?\n" && read target && sudo nmap --script vuln -oN "~/.obc/recon/$target.txt" $ip > /dev/null 2>&1')
        c = print('\n----------------------\n> Cannon Fired.\n')
        d = print('\n----------------------\n> O.B.C. Terminal\n----------------------\n> OPTIONS:\n> 1: Fingerprint\n> 2: PortScan\n> 3: Vulncannon\n> 4: Exit\n')
    else:
        print('\n----------------------\n> ERROR:UNKNOWN REQUEST\n')
        d = print('\n----------------------\n> O.B.C. Terminal\n----------------------\n> OPTIONS:\n> 1: Fingerprint\n> 2: PortScan\n> 3: Vulncannon\n> 4: Exit\n')
