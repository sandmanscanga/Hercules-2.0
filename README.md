# Hercules-2.0

## Hercules - An alternative to Hydra

The tool is used to target login portals where the attacker can reasonably determine a failed or successful login such that anything not matching that known request can be considered a HIT.

Provide the script the target domain/IP, the uripath to the portal, a mangled set of request parameters for the query, and a wordlist.

Then sit back and watch the fictional greek god go to work. I based the functionality on the infamous Hydra tool.

```bash

python hercules.py \
    -L /path/to/username/wordlist \
    -P /path/to/password/wordlist \
    -m "POST" \
    -u "http://localhost/wp-login.php" \
    -d "log=^USER^&pwd=^PASS^&wp-submit=Log+In&redirect_to=http%3A%2F%2Flocalhost%2Fwp-admin%2F&testcookie=1" \
    -f "ERROR" \
    -o /path/to/output/file \
    -t 32 \
    -a "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0" \
    -c "wordpress_test_cookie=WP+Cookie+check" \
    -i \
    -v

```

**This application was designed for educational purposes ONLY. I am not responsible for any misuse that the application may cause.**
