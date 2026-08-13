import json, httpx
from pathlib import Path



ROOT_DIR = Path(__file__).parent.parent
SITES_FILE_PATH = ROOT_DIR / "data" / "sites.json"

def check_user_availability(username: str):
    with open(SITES_FILE_PATH) as file:
        sites = json.load(file)

        for site in sites:
            print(site["name"])
            if site["name"].lower() == "bluesky":
                response = httpx.get(
                    "https://public.api.bsky.app/xrpc/app.bsky.actor.getProfile",
                    params={"actor": site["url"].format(username)},
                    follow_redirects=True
                )
            else:
                response = httpx.get(site["url"].format(username), follow_redirects=True)

            print(response.status_code)

check_user_availability("sanjusabu")