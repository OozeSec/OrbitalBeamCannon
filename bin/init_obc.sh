#!/bin/bash

OSTEMP="$(mktemp)"
hostnamectl >> $OSTEMP
APT="$(cat $OSTEMP | grep 'Ubuntu\|Kali' | wc -l)"
DNF="$(cat $OSTEMP | grep 'Fedora\|CentOS\|RHEL' | wc -l)" 
echo ".....If waiting for more than 10s, press [ENTER]....."

if [ $APT -eq 1 ] ; then
APT_NMAP="$(sudo apt-get install nmap -y)"
    $APT_NMAP
    mkdir ~/.obc
    git clone -b stable --single-branch https://github.com/OozeSec/OrbitalBeamCannon.git ~/.obc
    echo "alias obc='python3 ~/.obc/bin/obc.py'" >> ~/.bashrc && source ~/.bashrc
    echo "Orbital Beam Cannon Now Online & Operational."
elif [ $DNF -eq 1 ] ; then
DNF_NMAP='sudo dnf install nmap -y'
    $DNF_NMAP
    mkdir ~/.obc
    git clone -b stable --single-branch https://github.com/OozeSec/OrbitalBeamCannon.git ~/.obc
    echo "alias obc='python3 ~/.obc/bin/obc.py'" >> ~/.bashrc && source ~/.bashrc
    echo "Orbital Beam Cannon Now Online & Operational."
fi
