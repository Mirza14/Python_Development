import requests
from bs4 import BeautifulSoup

def search_mitre_attack(keyword):
    base_url = "https://attack.mitre.org"
    search_url = f"{base_url}/search/?q={keyword}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    print(f"Searching MITRE ATT&CK for keyword: {keyword}")
    response = requests.get(search_url, headers=headers)
    if response.status_code != 200:
        print("Failed to retrieve search results.")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all links to techniques, tools, etc.
    results = soup.find_all("a", href=True)
    found = []

    for link in results:
        href = link['href']
        if href.startswith("/techniques/") or href.startswith("/software/") or href.startswith("/groups/"):
            title = link.text.strip()
            full_link = base_url + href
            if title and full_link not in [item["url"] for item in found]:
                found.append({"title": title, "url": full_link})

    if found:
        print("\n🔍 Results found:")
        for item in found:
            print(f"- {item['title']}: {item['url']}")
    else:
        print("No relevant results found.")

search_mitre_attack("Dropbox")
