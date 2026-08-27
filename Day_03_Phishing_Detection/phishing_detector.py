import re
from urllib.parse import urlparse

# Suspicious keywords often used in phishing domains
KEYWORDS = ["login", "verify", "secure", "update", "account", "bank", "paypal"]


def phish_score(url):
    p = urlparse(url)
    score = 0

    # 1. HTTP check (No HTTPS / No Encryption) -> +30
    if not url.startswith("https"):
        score += 30

    # 2. Keywords in domain (e.g., paypal, login) -> +20
    for kw in KEYWORDS:
        if kw in p.netloc:
            score += 20
            break  # Avoid double counting multiple keywords

    # 3. Subdomain abuse / Excessive dots (more than 3 dots) -> +25
    if p.netloc.count(".") > 3:
        score += 25

    # 4. Direct IP address used instead of domain -> +40
    if re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", p.netloc):
        score += 40

    # Cap maximum score at 100%
    return min(score, 100)


# 10 Sample Test URLs (Mix of Legitimate and Phishing domains)
urls = [
    "https://paypal-login.evil.com/verify",
    "http://192.168.1.1/login.php",
    "https://secure-update-bank.com/account",
    "http://my.account.verify.login.paypal.fake-site.ru",
    "https://github.com",
    "https://google.com",
    "http://bank-account-update.net",
    "https://wikipedia.org",
    "http://10.0.0.1/verify/account",
    "https://login.microsoftonline.com",
]

print("=================================================================")
print("          DAY 3: URL PHISHING ANATOMY & DETECTION SCORES         ")
print("=================================================================\n")

for u in urls:
    risk = phish_score(u)
    status = "⚠️ SUSPICIOUS/HIGH RISK" if risk >= 50 else "✅ SAFE / LOW RISK"
    print(f"URL   : {u}")
    print(f"Result: {risk}% Risk [{status}]")
    print("-" * 65)