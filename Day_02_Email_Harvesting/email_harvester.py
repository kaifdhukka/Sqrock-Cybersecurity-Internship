import re
import requests


def harvest_emails(url):
    try:
        # Website ka HTML content fetch karna
        response = requests.get(url, timeout=10)
        html = response.text

        # Regex patterns se email addresses search karna (deduplication ke liye set use kiya hai)
        emails = set(re.findall(r"[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}", html))
        return emails

    except requests.exceptions.RequestException as e:
        print(f"[!] Error fetching URL: {e}")
        return set()


# Target lab URL (Testing site)
target_url = "https://httpbin.org"
found_emails = harvest_emails(target_url)

print(f"[*] Email Harvesting Results for {target_url}:\n")
if found_emails:
    for email in found_emails:
        print(f"[+] Found: {email}")
else:
    print("[-] No emails found or request failed.")