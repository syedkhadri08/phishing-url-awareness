from urllib.parse import urlparse


# Explanations for detected warning indicators
WARNING_EXPLANATIONS = {
    "URL contains an @ symbol":
        "The @ symbol can make a URL confusing by separating user information from the actual hostname.",

    "URL exceeds 100 characters":
        "Unusually long URLs can hide suspicious elements or make the destination harder to inspect.",

    "Hostname uses an IPv4 address":
        "The website uses an IP address instead of a conventional domain name. Verify the destination carefully.",

    "Hostname contains 5 or more labels":
        "A hostname with many dot-separated labels may be designed to look confusing or imitate another domain.",

    "Hostname contains a punycode marker":
        "Punycode can represent international characters in domain names. Visually similar characters may be used to imitate legitimate domains.",

    "URL uses HTTP instead of HTTPS":
        "HTTP does not encrypt the connection like HTTPS. Information exchanged with the website may be exposed."
}


# 1. Check for @ symbol
def has_at_symbol(url):
    return "@" in url


# 2. Check URL length
def is_url_too_long(url):
    return len(url) > 100


# 3. Check for IPv4-style hostname
def has_ip_address(url):
    hostname = urlparse(url).hostname

    if hostname is None:
        return False

    parts = hostname.split(".")

    return len(parts) == 4 and all(
        part.isdigit() and 0 <= int(part) <= 255
        for part in parts
    )


# 4. Check for five or more hostname labels
def has_many_subdomains(url):
    hostname = urlparse(url).hostname

    if hostname is None:
        return False

    parts = hostname.split(".")

    return len(parts) >= 5


# 5. Check for punycode marker
def has_punycode(url):
    hostname = urlparse(url).hostname

    if hostname is None:
        return False

    labels = hostname.lower().split(".")

    return any(label.startswith("xn--") for label in labels)


# 6. Check whether URL uses HTTP
def uses_http(url):
    parsed_url = urlparse(url)

    return parsed_url.scheme.lower() == "http"


# Validate URL input
def is_url_valid(url):
    try:
        parsed_url = urlparse(url)

        if parsed_url.scheme.lower() not in ["http", "https"]:
            return False

        hostname = parsed_url.hostname

        if not hostname:
            return False

        if any(char.isspace() for char in hostname):
            return False

        if hostname.startswith(".") or ".." in hostname:
            return False

        # Validate the port if provided
        parsed_url.port

        return True

    except ValueError:
        return False


# Analyze URL using all six detection functions
def analyze_url(url):
    checks = {
        "URL contains an @ symbol": has_at_symbol(url),
        "URL exceeds 100 characters": is_url_too_long(url),
        "Hostname uses an IPv4 address": has_ip_address(url),
        "Hostname contains 5 or more labels": has_many_subdomains(url),
        "Hostname contains a punycode marker": has_punycode(url),
        "URL uses HTTP instead of HTTPS": uses_http(url)
    }

    warnings = []

    for message, detected in checks.items():
        if detected:
            warnings.append(message)

    return warnings


# Main application
def main():
    while True:
        print("\n========== PHISHING URL AWARENESS CHECKER ==========")
        print("1. Analyze a URL")
        print("2. Quit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            url = input("\nEnter a URL to analyze: ").strip()

            if not url:
                print("Error: URL cannot be empty.")
                continue

            if not is_url_valid(url):
                print("Error: Please enter a valid HTTP or HTTPS URL.")
                continue

            results = analyze_url(url)

            print("\n========== URL ANALYSIS REPORT ==========")

            if results:
                print("\nWarning indicators detected:")

                for warning in results:
                    print(f"\n[!] {warning}")
                    print(f"    Explanation: {WARNING_EXPLANATIONS[warning]}")

                print("\nRecommendation: Review this URL carefully.")

            else:
                print("\nNo warning indicators detected.")

            print("\nNOTE: This tool cannot confirm whether a URL is safe.")
            print("Always verify unfamiliar links before interacting with them.")

        elif choice == "2":
            print("\nExiting Phishing URL Awareness Checker.")
            print("========== Goodbye! ==========")
            break

        else:
            print("\nInvalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()

