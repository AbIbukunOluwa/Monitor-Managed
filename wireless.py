#!/usr/bin/env/ python

import subprocess
import re
import argparse


def user_input():
    collect = argparse.ArgumentParser()
    collect.add_argument("-i", "--int", dest="interface", help="The interface you want to change to monitor mode")
    collect.add_argument("-m", "--mode", dest="mode", help="Options are either managed or monitor mode")
    options = collect.parse_args()
    if not options.interface:
        collect.error("[-] Kindly select the interface you want to change or use --help for more info")
    elif not options.mode:
        collect.error("[-] You failed to tell me if you want to be in monitor or managed")
    else:
        return options


def get_present(interface):
    take = subprocess.check_output(["iwconfig", interface])
    taken = re.search(r"(:M......)", take.decode("utf-8"))
    store = taken.group(0)
    reform = store.strip(':')
    # strip takes what has been found by the regex and strips the colon off it
    if not reform:
        print("[-] Could not find the mode of your interface")
    elif reform:
        print("[+] Your current mode is " + str(reform))
    return reform


def change(interface, mode, past):
    if mode == str("monitor"):
        print("[+] Bringing " + interface + " down")
        subprocess.call(["ifconfig", interface, "down"])
        print("[+] Killing any interference")
        subprocess.call(["airmon-ng", "check", "kill"])
        print("[+] Changing " + interface + " from " + past + " to " + mode)
        subprocess.call(["iwconfig", interface, "mode", mode])
        print("[+] Bringing " + interface + " up")
        subprocess.call(["ifconfig", interface, "up"])

    elif mode == str("managed"):
        print("[+] Bringing down " + interface)
        subprocess.call(["ifconfig", interface, "down"])
        print("[+] Changing mode" + " from " + past + " to " + mode)
        subprocess.call(["iwconfig", interface, "mode", "managed"])
        print("[+] Bringing up " + interface)
        subprocess.call(["ifconfig", interface, "up"])
        print("[+] Restarting network services")
        subprocess.call(["service", "NetworkManager", "restart"])


def verify_change(past, interface, mode):
    receiving = subprocess.check_output(["iwconfig", interface])
    keep = re.search(r"(:M......)", receiving.decode("utf-8"))
    find = keep.group(0)
    sliced = find.strip(':')
    # sliced is the same as the slice variable above
    sub = sliced.replace('M', 'm')
    # sub replaces the capital M to a small m
    if sub == mode:
        print("[+] Successfully changed your mode from " + past + " to " + mode)
    else:
        print("[-] Failed to change " + interface + " from " + past + " to " + mode)
        print("[-] The code needs a super-user permission, kindly run in root")
        print("[-] The mode can either be MANAGED or MONITOR")


print("This code should be run in python2, python3 has difficulties in processing the code.")
option = user_input()
stored = get_present(option.interface)
change(option.interface, option.mode, stored)
verify_change(stored, option.interface, option.mode)
