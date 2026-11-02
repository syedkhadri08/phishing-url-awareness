Phishing URL Awareness Checker

A Python-based command-line application that analyzes URL text and identifies common warning indicators associated with potentially suspicious links.

1. Overview

The Phishing URL Awareness Checker is a beginner-friendly cybersecurity awareness project developed using Python.

It examines user-provided URLs using predefined checks and displays warning indicators with explanations to help users review unfamiliar links carefully.

Important: This tool does not determine whether a URL is definitively safe or malicious. It performs basic heuristic checks on URL text only.

2. Features

The application performs six detection checks:

1. @ Symbol Detection: Identifies URLs containing the "@" symbol.
2. URL Length Detection: Flags URLs exceeding 100 characters.
3. IPv4 Address Detection: Identifies URLs using an IPv4-style hostname.
4. Hostname Label Detection: Flags hostnames containing five or more dot-separated labels.
5. Punycode Detection: Identifies hostname labels beginning with the "xn--" marker.
6. HTTP Detection: Identifies URLs using HTTP instead of HTTPS.

3. Additional Improvements

The following improvements were implemented:

- Interactive Menu: Allows users to analyze multiple URLs without restarting the application.
- Quit Option: Provides an option to exit the program.
- Warning Explanations: Displays an explanation alongside each detected warning.
- Input Validation: Rejects empty input, unsupported URL schemes and certain malformed URLs.

4. Technologies Used

- Python 3.10+
- "urllib.parse" module
- VS Code

No external Python packages are required.

5. Project Structure

phishing-url-awareness/
│
├── screenshots/
│   ├── test_results/
│   │   ├── Test 1.png
│   │   ├── Test 2.png
│   │   ├── Test 3.png
│   │   ├── Test 4.png
│   │   └── Test 5.png
│   │
│   └── sample_run.png
│
├── tests/
│   └── tests_samples.md
│
├── phishing_checker.py
├── README.md
└── requirements.txt

6. How to Run

Prerequisites

Install Python 3.10 or later.

Steps

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

python phishing_checker.py

5. Select option 1 to analyze a URL.
6. Enter the URL when prompted.
7. Select option 2 to exit the application.

7. Example Output

========== PHISHING URL AWARENESS CHECKER ==========
1. Analyze a URL
2. Quit

Enter your choice: 1

Enter a URL to analyze: http://192.0.2.10/account

========== URL ANALYSIS REPORT ==========

Warning indicators detected:

[!] Hostname uses an IPv4 address
    Explanation: The website uses an IP address instead of a conventional domain name. Verify the destination carefully.

[!] URL uses HTTP instead of HTTPS
    Explanation: HTTP does not encrypt the connection like HTTPS. Information exchanged with the website may be exposed.

Recommendation: Review this URL carefully.

8. Testing

The application was tested using the five sample URLs specified in the project workbook.

All five required test cases passed.

Additional tests were performed for:

- Empty input.
- Missing URL schemes.
- Malformed hostnames.
- Invalid port numbers.
- Punycode detection.

Refer to "tests/test_samples.md" for the test results.

9. Screenshots

Screenshots demonstrating the application execution and test results are available in the "screenshots/" directory.

10. Limitations

- The application analyzes URL text only.
- It does not access or scan external websites.
- It does not use threat intelligence databases.
- Warning indicators do not prove that a URL is malicious.
- No detected warnings do not guarantee that a URL is safe.

11. Ethical Use

This project is intended for cybersecurity awareness and educational purposes.

Only sample URL strings are used for testing. The application does not visit suspicious websites or collect user credentials.

12. Author

Name: Syed Mohammed Khadri
Last Updated: Nov 2026