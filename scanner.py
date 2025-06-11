import nmap

def scan(host, start_port=1, end_port=1024):
    scanner = nmap.PortScanner()
    port_range = f"{start_port}-{end_port}"
    print(f"Scanning {host} for ports {port_range}...\n")

    try:
        scanner.scan(host, port_range, arguments="-sV")
    except Exception as e:
        print(f"Error: {e}")
        return {}

    if host not in scanner.all_hosts():
        return {"error": "Host is down or not responding."}

    results = {}
    for proto in scanner[host].all_protocols():
        for port in sorted(scanner[host][proto].keys()):
            port_info = scanner[host][proto][port]
            if port_info.get('state') != 'open':
                continue

            product = port_info.get('product', '')
            version = port_info.get('version', '')
            service = port_info.get('name', 'unknown')
            full_service = f"{product} {version}".strip()

            results[port] = {
                "protocol": proto,
                "state": "open",
                "service": service,
                "product": product,
                "version": version,
                "full_service": full_service
            }

    return results
