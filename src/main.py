import argparse, sys
from email_validator import validate_email, EmailNotValidError

# Basic structure of the application

# command [type] [target]
# example:

#    command username s4njusabu
#    command email sanjusabu@icloud.com

# ----- first iteration of the app will only include username search ----- 

def cli_args():
    parser = argparse.ArgumentParser(
        description="""OSINT tool with similarity checks.

Username search : command username s4njusabu
Email search    : command email sanjusabu@icloud.com""",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument("action", help='Example: "username" or "email"')
    parser.add_argument("target", help='Example: "s4njusabu" or "sanjusabu@icloud.com". In other words the username or email you wanna search')

    args = parser.parse_args()

    action = args.action.lower()

    if action not in ["username", "email"]:
        print('Action should be either "username" or "email"')
        sys.exit(1)

    if action == "email":
        try:
            email = validate_email(args.target)
        except EmailNotValidError as e:
            print(f"Invalid email: {e}")
            sys.exit(1)
    else:
        username = args.target

    if action == "username":
        return (action, username)
    else:
        return (action, email.normalized)

if __name__ == "__main__":
    print(cli_args())