import ipaddress

# Define the IP range
start_ip = '192.168.1.1'
end_ip = '192.168.1.254'

# Convert the start and end IPs to IPv4Address objects
start_ip_obj = ipaddress.IPv4Address(start_ip)
end_ip_obj = ipaddress.IPv4Address(end_ip)

# Iterate through the IP range and print each IP address
for ip_int in range(int(start_ip_obj), int(end_ip_obj) + 1):
    ip_addr = ipaddress.IPv4Address(ip_int)
    print(ip_addr)