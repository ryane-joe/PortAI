from scanner import scan
from Get_Vulns import get_vulnerabilities

host = input("Enter a host to scan (e.g. 127.0.0.1): ").strip()
scan_results = scan(host)

if isinstance(scan_results, dict) and "error" in scan_results:
    print(scan_results["error"])
else:
    for port, info in scan_results.items():
        service_description = info["full_service"]
        print(f"\n🔍 Checking CVEs for service on port {port}: {service_description}")
        cve_info = get_vulnerabilities(service_description)
        print(cve_info)
