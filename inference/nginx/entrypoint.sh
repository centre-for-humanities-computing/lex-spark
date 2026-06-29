#!/bin/sh
set -e

# Substitute __AUTH_TOKEN__ placeholder in nginx.conf.template.
# Uses sed (available in nginx:alpine). envsubst is NOT available in Alpine.
AUTH_TOKEN="${AUTH_TOKEN:-}"

echo "--- nginx entrypoint: injecting AUTH_TOKEN ---"
if [ -z "$AUTH_TOKEN" ]; then
    echo "WARNING: AUTH_TOKEN is not set. All inference requests will be rejected."
    # Use an impossible-to-guess sentinel so the map always falls through to default=0.
    AUTH_TOKEN="__UNSET__$(od -A n -t x -N 16 /dev/urandom | tr -d ' \n')"
fi

sed "s|__AUTH_TOKEN__|${AUTH_TOKEN}|g" /etc/nginx/nginx.conf.template > /etc/nginx/nginx.conf

exec nginx -g 'daemon off;'
