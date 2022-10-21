"""from netmiko import ConnectHandler


The VM is configured to use dhcp on eth0
You must determine your router's eth0 interface address.


vyos_router = {
    "device_type": "vyos",
    "host": "192.168.56.102",
    "username": "vyos",
    "password": "vyos",
    "port": 22,
}

net_connect = ConnectHandler(**vyos_router)

IFconfig_commands = [
    'set interfaces ethernet eth0 description WAN',
    'set interfaces ethernet eth1 description LAN',
]

# set InterFace configuration
IFOutput = net_connect.send_config_set(IFconfig_commands, exit_config_mode=False)
print(IFOutput)

# set dhcp server configuration


DHCPconfig_commands = [
    "set service dhcp-server shared-network-name LAN subnet 192.168.0.0/24 default-router '192.168.0.1'",
    "set service dhcp-server shared-network-name LAN subnet 192.168.0.0/24 domain-name 'vyos.net'",
    "set service dhcp-server shared-network-name LAN subnet 192.168.0.0/24 lease '86400'",
    "set service dhcp-server shared-network-name LAN subnet 192.168.0.0/24 range 0 start '192.168.0.9'",
    "set service dhcp-server shared-network-name LAN subnet 192.168.0.0/24 range 0 stop '192.168.0.254'"
]

DHCPOutput = net_connect.send_config_set(DHCPconfig_commands, exit_config_mode=False)
print(DHCPOutput)

# set dns configuration

DNSconfig_commands = [
    "set service dns forwarding cache-size '0'",
    "set service dns forwarding listen-address '192.168.0.1'",
    "set service dns forwarding allow-from '192.168.0.0/24'",
]

print(net_connect.send_config_set(DNSconfig_commands, exit_config_mode=False))


# set nat configuration

NATconfig_commands = [
    "set nat source rule 100 outbound - interface 'eth0'",
    "set nat source rule 100 source address '192.168.0.0/24'",
    "set nat source rule 100 translation address masquerade"

]

#print(net_connect.send_config_set(NATconfig_commands, exit_config_mode=False))


# commit configuration
print(net_connect.commit())


#op-mode commands
output = net_connect.send_command("run show interfaces ethernet")
print(output)

"""


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
