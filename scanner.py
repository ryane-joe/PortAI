import nmap

def scan(host, start_port=1, end_port=9000):
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

    print(f"Scan results for {host}:\n")
    results = {}

    for proto in scanner[host].all_protocols():
        ports = scanner[host][proto].keys()
        for port in sorted(ports):
            port_info = scanner[host][proto][port]
            state = port_info.get('state', 'unknown')
            if state != 'open':
                continue

            service = port_info.get('name', 'unknown')
            product = port_info.get('product', '')
            version = port_info.get('version', '')
            full_service = f"{product} {version}".strip()
            results[port] = {
                "protocol": proto,
                "state": state,
                "service": service,
                "product": product,
                "version": version,
                "full_service": full_service
            }

    return results
