# populate_localstorage.py
"""
This script generates a JavaScript snippet to populate localStorage with sample users and comments for the school-attack environment.
Run this script, then copy and paste the output into your browser's console on the site.
"""
import json

# Sample users and comments
data = {
    "users": [
        {"username": "admin", "password": "admin123"},
        {"username": "student", "password": "password"},
        {"username": "guest", "password": "guest"}
    ],
    "comments": [
        {"user": "admin", "text": "Welcome to the portal!"},
        {"user": "student", "text": "This site is fun! <script>alert('XSS')</script>"},
        {"user": "guest", "text": "Try to hack me if you can!"}
    ]
}

print("// Paste this in your browser's console on the site:")
for key, value in data.items():
    json_str = json.dumps(value).replace("'", "\\'")
    js = f"localStorage.setItem('{key}', '{json_str}');"
    print(js)
