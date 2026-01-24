# Deployment Configuration for HTTPS

To support the settings defined in 'settings.py', the production web server (Nginx or Apache) must be configured with a valid SSL/TLS certificate (e.g., from Let's Encrypt).

## Nginx Example Configuration
```nginx
server {
    listen 80;
    server_name yourdomain.com;
    return 301 https://$host$request_uri; # Redirect HTTP to HTTPS
}

server {
    listen 443 ssl;
    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;
    # ... other configurations
}
```
