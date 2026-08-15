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

if __name__ == "__main__":
    action, target = cli_args()

    print("--------- OSINT ---------")

    if action == "username":
        media_sites = check_username(target)

        if media_sites == 2:
            bluesky = get_media_bluesky(target)
            mastodon = get_media_mastodon(target)

            if bluesky and mastodon:
                compare_dates(bluesky, mastodon)
        
    else:
        print("Email search coming soon")