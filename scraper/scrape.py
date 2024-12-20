import requests
from bs4 import BeautifulSoup

def scrape_github_profile(username):
    url = f"https://github.com/{username}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract name
        name_tag = soup.find('span', {'itemprop': 'name'})
        name = name_tag.get_text(strip=True) if name_tag else ''
        
        # Extract Bio
        bio_tag = soup.find('div', {'data-bio-text': True})
        bio = bio_tag.get_text(strip=True) if bio_tag else ''
    
        
        # Extract public repos, followers, and following
        stats = soup.find_all('span', class_='text-bold color-fg-default')
        followers = 0
        following = 0
        
        for stat in stats:
            text = stat.get_text(strip=True)
            if text.isdigit():
                parent = stat.find_parent('a')
                if parent:
                    href = parent.get('href', '')
                    if 'followers' in href:
                        followers = int(text)
                    elif 'following' in href:
                        following = int(text)
        
        repos = soup.find_all('span', class_='Counter')
        public_repos = 0
        for repo in repos:
            text = repo.get_text(strip=True)
            if text.isdigit():
                parent = repo.find_parent('a')
                if parent:
                    href = parent.get('href', '')
                    if 'repositories' in href:
                        public_repos = int(text)
                        break
        
        # Extract avatar URL
        avatar_tag = soup.find('img', class_='avatar-user')
        avatar_url = avatar_tag.get('src') if avatar_tag else ''

        return {
            'name': name,
            'bio': bio,
            'public_repos': public_repos,
            'followers': followers,
            'following': following,
            'avatar_url': avatar_url,
            'profile_url': url,
        }
    return None