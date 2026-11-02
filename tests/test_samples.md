Phishing URL Awareness Checker – Test Results

Test Cases

Test| Expected Result| Actual Result| Status
1   | No warnings| No warnings detected| PASS
2   | IPv4 address, HTTP| Both warnings detected| PASS
3   | @ symbol, HTTP| Both warnings detected| PASS
4   | Many hostname labels| Warning detected| PASS
5   | Punycode marker| Warning detected| PASS

Test Notes

- All five required sample URLs were tested successfully.
- The application correctly identified multiple warning indicators in a single URL.
- The application displayed explanations for detected warnings.
- The application did not classify URLs as definitively safe or malicious.