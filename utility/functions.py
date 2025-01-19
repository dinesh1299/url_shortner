import socket
import hashlib
from datetime import datetime, timedelta
import re
def generate_ip():
    return socket.gethostbyname(socket.gethostname())

def validate_url(url):
    pattern = re.compile(r'^(http|https)://')
    return bool(pattern.match(url))

def generate_short_url(org_url, request):
    return f"http://{request.get_host()}/{hashlib.md5(org_url.encode()).hexdigest()[:6]}"

def generate_expires_at(hrs):
    return datetime.now() + timedelta(hours=hrs)
