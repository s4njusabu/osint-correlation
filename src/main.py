from cli_args import cli_args

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
    print(cli_args())