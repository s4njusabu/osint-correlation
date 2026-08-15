import json, httpx, requests
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
SITES_FILE_PATH = ROOT_DIR / "data" / "sites.json"

def check_username(username: str):
    with open(SITES_FILE_PATH) as file:
        sites = json.load(file)

    checked = 0
    found = 0


    for site in sites:
        checked += 1   
        try:
            if site["name"].lower() == "bluesky":
                response = httpx.get(
                    "https://public.api.bsky.app/xrpc/app.bsky.actor.getProfile",
                    params={"actor": site["url"].format(username)},
                    follow_redirects=True,
                    timeout=5
                )
            else:
                response = httpx.get(
                    site["url"].format(username), 
                    follow_redirects=True, 
                    timeout=5
                )
            
        except httpx.TimeoutException:
            print(f"  [!] {site['name']:<12} TIMEOUT")
            continue

        except httpx.RequestError as e:
            print(f"  [!] {site['name']:<12} ERROR: {e}")
            continue
    
        if response.status_code == 200:
            found += 1
            print(f"  [+] {site["name"]:<12} FOUND")
        else:
            print(f"  [-] {site["name"]:<12} NOT FOUND")

    print(f"Result: {found} / {checked} FOUND")
        

def get_media_bluesky(username: str):
    username = f"{username}.bsky.social"
    url = "https://public.api.bsky.app/xrpc/app.bsky.feed.getAuthorFeed"

    response = requests.get(url, params={
        "actor": username,
        "filter": "posts_with_media",
        "limit": 5,
    })

    if not response.ok:
        return []

    data = response.json()
    info = []

    for item in data["feed"]:
        post = item["post"]
        embed = post.get("embed", {})

        image = None

        if embed.get("$type") == "app.bsky.embed.images#view":
            images = embed.get("images", [])
            if images:
                image = images[0]["fullsize"]

        info.append({
            "text": post["record"]["text"],
            "date": post["record"]["createdAt"],
            "media": image,
        })

    with open("bluesky_media.json", "w") as f:
        json.dump(info, f, indent=4)

    return info


def get_media_mastodon(username: str):
    response = requests.get(
        "https://mastodon.social/api/v1/accounts/lookup",
        params={"acct": username},
    )

    if not response.ok:
        return []

    account = response.json()
    account_id = account["id"]

    response = requests.get(
        f"https://mastodon.social/api/v1/accounts/{account_id}/statuses",
        params={
            "only_media": "true",
            "limit": 5,
        },
    )

    if not response.ok:
        return []

    data = response.json()
    info: list[dict] = []

    for post in data:
        image = None

        for media in post["media_attachments"]:
            if media["type"] == "image":
                image = media["url"]
                break

        info.append({
            "text": post["content"],
            "date": post["created_at"],
            "media": image,
        })

    with open("mastodon_media.json", "w") as f:
        json.dump(info, f, indent=4)

    return info
