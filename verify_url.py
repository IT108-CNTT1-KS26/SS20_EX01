import idna
from urllib.parse import urlparse

def is_safe_url(target_url: str, expected_domain: str = "github.com") -> bool:
    try:
        parsed = urlparse(target_url)
        hostname = parsed.hostname or ""
        punycode_domain = idna.encode(hostname).decode('ascii')
        if punycode_domain.startswith("xn--") or ".xn--" in punycode_domain:
            return False
        return hostname.lower() == expected_domain.lower()
    except Exception:
        return False

if __name__ == "__main__":
    print(is_safe_url("https://githúb.com/login"))