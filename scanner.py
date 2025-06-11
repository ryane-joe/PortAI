import nmap

def scan_with_nmap(host, start_port=1, end_port=1024):
    scanner = nmap.PortScanner()
    port_range = f"{start_port}-{end_port}"
    print(f"Scanning {host} for ports {port_range}...\n")

    try:
        scanner.scan(host, port_range, arguments="-sV")
    except Exception as e:
        print(f"Error: {e}")
        return

    if host not in scanner.all_hosts():
        print("Host is down or not responding.")
        return

    print(f"Scan results for {host}:\n")
    for proto in scanner[host].all_protocols():
        ports = scanner[host][proto].keys()
        for port in sorted(ports):
            state = scanner[host][proto][port]['state']
            service = scanner[host][proto][port].get('name', 'unknown')
            product = scanner[host][proto][port].get('product', '')
            version = scanner[host][proto][port].get('version', '')
            extra = f"{product} {version}".strip()
            print(f"[+] Port {port}/{proto} is {state} | Service: {service} {extra}")

if __name__ == "__main__":
    target = input("Enter the host to scan (e.g., 127.0.0.1): ")
    start = int(input("Enter start port (default 1): ") or "1")
    end = int(input("Enter end port (default 1024): ") or "1024")
    scan_with_nmap(target, start, end)
