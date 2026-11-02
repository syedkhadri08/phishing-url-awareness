# Test Results

Python version used: 3.__ | Operating system: ________ | Date: ________

<!-- Fill the three blanks above from YOUR computer after re-running the five tests. -->

## Required sample tests

| # | Input | Expected result | Actual result | Pass/Fail |
|---|-------|-----------------|---------------|-----------|
| 1 | https://www.example.com/login | No listed warning signs | No warning indicators detected. | PASS |
| 2 | http://192.0.2.10/account | IP address + HTTP | Hostname uses an IPv4 address; URL uses HTTP instead of HTTPS | PASS |
| 3 | http://example.com@sample.invalid/login | @ symbol + HTTP | URL contains an @ symbol; URL uses HTTP instead of HTTPS | PASS |
| 4 | https://a.b.c.d.e.example.invalid/path | Many hostname segments | Hostname contains 5 or more labels | PASS |
| 5 | https://xn--example.invalid/ | Punycode-style hostname | Hostname contains a punycode marker | PASS |

## Additional tests (edge cases and bonus checks)

| # | Input | Expected result | Actual result | Pass/Fail |
|---|-------|-----------------|---------------|-----------|
| 6 | (empty, just press Enter) | Rejected politely | Error: URL cannot be empty. | PASS |
| 7 | www.example.com | http:// assumed, HTTP warning | Note: No scheme was entered, so http:// was assumed. + URL uses HTTP instead of HTTPS | PASS |
| 8 | https://secure-login.example.invalid | No warnings (tricky name slips through) | No warning indicators detected. | PASS |
| 9 | http://[bad | Rejected, no crash | Error: Please enter a valid HTTP or HTTPS URL. | PASS |
| 10 | http://example.com:99999/ | Invalid port rejected | Error: Please enter a valid HTTP or HTTPS URL. | PASS |
| 11 | ftp://example.invalid/file | Unsupported scheme rejected | Error: Please enter a valid HTTP or HTTPS URL. | PASS |
| 12 | http://exa mple.com | Space in hostname rejected | Error: Please enter a valid HTTP or HTTPS URL. | PASS |
| 13 | HTTP://EXAMPLE.COM | Scheme check is case-insensitive | URL uses HTTP instead of HTTPS | PASS |
| 14 | https://example.invalid/ followed by 100 letter a's | Length warning | URL exceeds 100 characters | PASS |
| 15 | http://256.1.1.1/ | Not a valid IPv4 address, so no IP warning | URL uses HTTP instead of HTTPS | PASS |

## Notes

- The five required samples each triggered exactly the warnings I expected, and the tool never opened any URL.
- Test 8 shows the main limit of this tool: a deceptive-looking name can produce no warnings at all, so "no warnings" never means "safe".
- A bug I found and fixed while testing: the IPv4 check could crash on look-alike digit characters (for example a superscript 2) because `str.isdigit()` accepts them but `int()` does not. Adding `part.isascii()` fixed it.
- Known false positive: an @ symbol in the query string (for example `?email=a@b.invalid`) is flagged, because the check looks for @ anywhere in the URL.