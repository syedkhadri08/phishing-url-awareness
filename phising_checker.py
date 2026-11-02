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

    # isascii() is required: str.isdigit() also accepts characters such as
    # superscript digits, which int() cannot convert and would crash the program.
    return len(parts) == 4 and all(
        part.isascii() and part.isdigit() and 0 <= int(part) <= 255
        for part in parts
    )


# 4. Check for five or more hostname labels
def has_many_subdomains(url):
    hostname = urlparse(url).hostname

    if hostname is None:
        return False

    # Ignore empty labels so a trailing dot (example.com.) is not counted
    parts = [part for part in hostname.split(".") if part]

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


# Add http:// when the user typed a URL without a scheme
def add_default_scheme(url):
    if "://" in url:
        return url, False

    return "http://" + url, True


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

        # Accessing .port raises ValueError for an invalid port number
        _ = parsed_url.port

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
    try:
        while True:
            print("\n========== PHISHING URL AWARENESS CHECKER ==========")
            print("Text checks only - this program does not open URLs.")
            print("1. Analyze a URL")
            print("2. Quit")

            choice = input("\nEnter your choice: ").strip()

            if choice == "1":
                url = input("\nEnter a sample URL to analyze: ").strip()

                if not url:
                    print("Error: URL cannot be empty.")
                    continue

                url, scheme_assumed = add_default_scheme(url)

                if not is_url_valid(url):
                    print("Error: Please enter a valid HTTP or HTTPS URL.")
                    continue

                if scheme_assumed:
                    print("\nNote: No scheme was entered, so http:// was assumed.")

                results = analyze_url(url)

                print("\n========== URL ANALYSIS REPORT ==========")

                if results:
                    print("\nWarning indicators detected:")

                    for warning in results:
                        print(f"\n[!] {warning}")
                        print(f"    Explanation: {WARNING_EXPLANATIONS[warning]}")

                    print(f"\nREVIEW CAREFULLY: {len(results)} warning sign(s) found.")

                else:
                    print("\nNo warning indicators detected.")

                print("\nNOTE: This tool cannot confirm whether a URL is safe.")
                print("Never enter passwords from unexpected links.")

            elif choice == "2":
                print("\nExiting Phishing URL Awareness Checker.")
                print("========== Goodbye! ==========")
                break

            else:
                print("\nInvalid choice. Please select 1 or 2.")

    except (EOFError, KeyboardInterrupt):
        print("\n\nInput closed. Goodbye! Stay alert online.")


if __name__ == "__main__":
    main()