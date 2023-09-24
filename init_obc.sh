#!/bin/bash

OSTEMP="$(mktemp)"
hostnamectl >> $OSTEMP
cat $OSTEMP
APT="$(cat $OSTEMP | grep Ubuntu | wc -l)"
DNF="$(cat $OSTEMP | grep 'Fedora\|CentOS\|RHEL' | wc -l)" 

if [ $APT -eq 1 ] ; then
#    sudo apt install nmap -y
APT_NMAP='sudo apt install nmap -y'   
    $APT_NMAP
    mkdir ~/.obc
    git clone -b stable --single-branch git@github.com:OozeSec/OrbitalBeamCannon.git [~/.obc]
    echo "alias obc='~/.obc/obc.py'.." >> ~/.bashrc && source ~/.bashrc
    echo "Orbital Beam Cannon Now Online & Operational."
elif grep -q -- 1 "$DNF" ; then
#    dnf install nmap -y >> /dev/null 2&>1
DNF_NMAP='sudo dnf install nmap -y'
    $DNF_NMAP
    mkdir ~/.obc
    git clone -b stable --single-branch git@github.com:OozeSec/OrbitalBeamCannon.git [~/.obc]
    echo "alias obc='~/.obc/obc.py'.." >> ~/.bashrc && source ~/.bashrc
    echo "Orbital Beam Cannon Now Online & Operational."
fi