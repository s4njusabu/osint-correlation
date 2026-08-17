from cli_args import cli_args
from fetch import check_username, get_media_bluesky, get_media_mastodon
from compare import compare_dates

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

if __name__ == "__main__":
    action, target = cli_args()

    print("--------- OSINT ---------")

    if action == "username":
        media_sites = check_username(target)

        if media_sites == 2:
            bluesky = get_media_bluesky(target)
            mastodon = get_media_mastodon(target)

            if bluesky and mastodon:
                sim = compare_dates(
                    bluesky[0]["date"],
                    mastodon[0]["date"]
                )
                if sim > DATE_THRESHOLD:
                    print("Hehehe")
    else:
        print("Email search coming soon")