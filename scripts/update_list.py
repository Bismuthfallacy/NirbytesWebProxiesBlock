import requests
import re
from bs4 import BeautifulSoup

# URL of the proxy list page
url = "https://nirbytes.com/post/1000-proxies-for-school-chromebook-2025"

# Domains to exclude
excluded_domains = [
    "graph.org",
    "schoolwebproxy.com",
    "binance.com",
    "example.com",
    "googletagmanager.com",
    "pinterest.com",
    "schema.org",
    "clarity.ms",
    "api.w.org",
    "cdn.onesignal.com",
    "ogp.me",
    "discord.com",
    "googlesyndication.com"
]

# Fetch page content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Remove the comments section if it exists
comments_section = soup.find(id="comments")
if comments_section:
    comments_section.decompose()  # remove from soup

# Now extract only the remaining visible text
clean_text = soup.get_text()

# Extract all https:// links
proxy_links = re.findall(r'https://[^\s"<>\n]+', clean_text)

# Filter out excluded domains
filtered_links = [
    link for link in proxy_links
    if not any(domain in link for domain in excluded_domains)
]

# Deduplicate and sort
filtered_links = sorted(set(filtered_links))

# Write to proxies.txt
with open("proxies.txt", "w") as f:
    for link in filtered_links:
        f.write(link + "\n")
