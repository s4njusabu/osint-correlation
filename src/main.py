from cli_args import cli_args
from fetch import check_username, get_media_bluesky, get_media_mastodon
from compare import compare_dates, compare_texts, compare_images
import re

# step 1
# ------------------------------------------------------------------------
# BASIC STRUCTURE OF THE APPLICATION

# command [type] [target]
# examples:

#    command username s4njusabu
#    command email sanjusabu@icloud.com

# first iteration of the app will only include username search 
# ------------------------------------------------------------------------

DATE_THRESHOLD = 0.7
TEXT_THRESHOLD = 0.7

if __name__ == "__main__":
    action, target = cli_args()

    print("--------- OSINT ---------")

    if action == "username":
        media_sites = check_username(target)

        if media_sites == 2:
            bluesky = get_media_bluesky(target)
            mastodon = get_media_mastodon(target)

            if bluesky and mastodon:
                date_sim = compare_dates(
                    bluesky[0]["date"],
                    mastodon[0]["date"]
                )
                if date_sim > DATE_THRESHOLD:
                    mastodon_text = re.sub("<.*?>", "", mastodon[0]["text"])
                    text_sim = compare_texts(
                        bluesky[0]["text"],
                        mastodon_text
                    )
                    if text_sim > TEXT_THRESHOLD:
                        image_sim = compare_images(bluesky[0]["media"], mastodon[0]["media"])
                        if image_sim >= 0.8:
                            print("[+] HIGH CONFIDENCE: Bluesky and Mastodon")
                        elif image_sim >= 0.5:
                            print("[~] POSSIBLE MATCH: Bluesky and Mastodon")
                        else:
                            print("[-] LOW CONFIDENCE: Bluesky and Mastodon")
    else:
        print("Email search coming soon")