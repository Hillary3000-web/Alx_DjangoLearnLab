# Security Measures Implemented

1. **Production Settings**: DEBUG is set to False to prevent information leakage.
2. **Cookie Security**: CSRF and Session cookies are restricted to HTTPS.
3. **Browser Protections**: Enabled XSS filtering and prevented content sniffing.
4. **SQL Injection Prevention**: All views use Django ORM for parameterized queries.
5. **XSS & CSRF Protection**: CSRF tokens are enforced on all forms.
