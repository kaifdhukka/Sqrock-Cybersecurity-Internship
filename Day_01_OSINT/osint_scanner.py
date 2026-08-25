import socket
import whois
import requests

def osint_scan(domain):
    print(f"==========================================")
    print(f"  OSINT PASSIVE RECON REPORT: {domain}")
    print(f"==========================================")
    
    # 1. WHOIS Lookup
    try:
        w = whois.whois(domain)
        registrar = w.registrar if w.registrar else "N/A"
        creation_date = w.creation_date
        print(f"[+] Registrar      : {registrar}")
        print(f"[+] Creation Date  : {creation_date}")
    except Exception as e:
        print(f"[-] WHOIS Error    : {e}")

    # 2. DNS Resolution (IP Gathering)
    try:
        ip = socket.gethostbyname(domain)
        print(f"[+] Target IP      : {ip}")
    except Exception as e:
        print(f"[-] IP Error       : {e}")
        return

    # 3. IP Geolocation Lookup
    try:
        geo = requests.get(f"http://ip-api.com/json/{ip}").json()
        city = geo.get('city', 'Unknown')
        country = geo.get('country', 'Unknown')
        isp = geo.get('isp', 'Unknown')
        print(f"[+] Location       : {city}, {country}")
        print(f"[+] ISP            : {isp}")
    except Exception as e:
        print(f"[-] Geo Error      : {e}")

    print(f"==========================================")

if __name__ == "__main__":
    target_domain = "example.com"
    osint_scan(target_domain)