from cli_args import cli_args
from fetch import check_username

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

    if action == "username":
        check_username(target)
        
    else:
        print("Email search coming soon")