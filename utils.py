import re

def extract_username(profile_url):
    match = re.search(r"reddit\.com/user/([^/]+)/?", profile_url)
    return match.group(1) if match else None
