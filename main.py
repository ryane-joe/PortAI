from scanner import scan
from Get_Vulns import get_vulnerabilities

def main():
    host = input("Enter a host to scan (e.g. 127.0.0.1): ").strip()
    if not host:
        print("No host provided, exiting.")
        return

    print(f"\nStarting scan on {host}...\n")
    scan_results = scan(host)

    if isinstance(scan_results, dict) and "error" in scan_results:
        print(scan_results["error"])
        return

    if not scan_results:
        print("No open ports/services found.")
        return

    for port, info in scan_results.items():
        service_description = info.get("full_service") or info.get("service") or "unknown service"
        print(f"\n🔍 Checking CVEs for service on port {port}: {service_description}")
        cve_info = get_vulnerabilities(service_description)
        print(cve_info)

if __name__ == "__main__":
    main()
