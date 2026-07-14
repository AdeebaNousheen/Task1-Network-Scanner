import nmap
import json

scanner = nmap.PortScanner()

target = "192.168.56.102"

print(f"Scanning {target}...")

scanner.scan(target, arguments="-sV")

results = {}

for host in scanner.all_hosts():
    results[host] = {}
    print(f"\nHost: {host}")

    for protocol in scanner[host].all_protocols():
        results[host][protocol] = {}

        ports = scanner[host][protocol].keys()

        for port in ports:
            service = scanner[host][protocol][port]['name']
            version = scanner[host][protocol][port].get('product', 'Unknown')

            print(f"Port: {port}")
            print(f"Service: {service}")
            print(f"Version: {version}")
            print("----------------------")

            results[host][protocol][port] = {
                "service": service,
                "version": version
            }

with open("scan_results.json", "w") as file:
    json.dump(results, file, indent=4)

print("\nScan completed.")
print("Results saved in scan_results.json")
