# Python Assignment
# Nathan Cross, 000809011
def blackHoler():
    from python_hosts import Hosts, HostsEntry
    import time
    import sys

    hostPath = 'c:/Windows/System32/Drivers/etc/hosts'

    try:
        if str(sys.argv[1]) == "":
            hostname = input("Enter a Hostname to blacklist: ")
        else:
            hostname = sys.argv[1]
    except:
        hostname = input("Enter a Hostname to blacklist: ")
    hosts = Hosts(path=hostPath)
    try:
        f = open(hostPath, "a")
        f.close()
    except:
        input("Program needs to be run as admin! Press ENTER to exit.")
        exit()

    while True:
        new_entry = HostsEntry(entry_type='ipv4', address='0.0.0.0', names=[hostname])
        specifics = (hosts.add([new_entry]))
        if specifics["duplicate_count"] >= 1:
            choice = input("This entry already exists, would you like to modify it? y/n: ")
            if choice.lower() == "y":
                f = open("FQDNAdded.txt", "a")
                f.write(hostname + " - hostname blackhole removed\n")
                f.close()
                hosts.remove_all_matching(name=hostname)
                hosts.write()
                hostname = input("Enter the new FQDM that will be blackholed: ")
            elif choice.lower() == "n":
                print("'n' chosen, exiting.")
                exit()
            else:
                print("y/n not chosen.")
        else:
            break
    hosts.write()
    print(hostname + " Written")
    f = open("FQDNAdded.txt", "a")
    f.write(hostname + " - hostname blackhole added\n")
    f.close()
    time.sleep(3)


if __name__ == "__main__":
    blackHoler()
